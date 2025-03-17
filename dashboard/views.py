# Create your views here.
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm  # Ensure forms.py exists in dashboard
from .utils import get_twitter_posts, get_facebook_posts
from .tasks import scheduled_post  # Import Celery task for scheduling
from datetime import datetime
from django.utils.timezone import make_aware

# ✅ Signup View
def signup_view(request):
    """
    Handles user signup. If the form is valid, it logs in the user and redirects to the dashboard.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Ensure 'dashboard' URL exists
    else:
        form = SignUpForm()
    
    return render(request, 'dashboard/signup.html', {'form': form})  # ✅ Corrected template path

# ✅ Dashboard View
def dashboard_view(request):
    """
    Fetches Twitter & Facebook posts and displays them on the dashboard.
    """
    twitter_data = get_twitter_posts().get("data", [])  # Extract 'data' key safely
    facebook_data = get_facebook_posts().get("data", [])  # Extract 'data' key safely

    return render(request, "dashboard/dashboard.html", {  # ✅ Ensure template path is correct
        "twitter_data": twitter_data,
        "facebook_data": facebook_data
    })

# ✅ Schedule Post View
def schedule_post_view(request):
    """
    Handles scheduling posts for Twitter & Facebook.
    """
    if request.method == 'POST':
        message = request.POST.get('message')  # Get message from form
        scheduled_time = request.POST.get('scheduled_time')  # Get scheduled time (optional)

        if scheduled_time:
            try:
                # Convert input string to a datetime object
                scheduled_time = make_aware(datetime.strptime(scheduled_time, "%Y-%m-%d %H:%M:%S"))
                scheduled_post.apply_async(args=[message], eta=scheduled_time)  # Schedule post
            except ValueError:
                return render(request, "dashboard/schedule_post.html", {"error": "Invalid date format. Use YYYY-MM-DD HH:MM:SS"})
        else:
            scheduled_post.delay(message)  # Post immediately if no time provided

        return redirect('dashboard')  # Redirect to dashboard after scheduling
    
    return render(request, "dashboard/schedule_post.html")

# ✅ Analytics View
def analytics_view(request):
    """
    Fetch social media posts and calculate total likes.
    """
    # Get data from APIs
    twitter_data = get_twitter_posts().get("data", [])  # Extract 'data' list safely
    facebook_data = get_facebook_posts().get("data", [])  # Extract 'data' list safely

    # Calculate total likes from Twitter posts
    twitter_likes = sum(post.get('public_metrics', {}).get('like_count', 0) for post in twitter_data)

    # Calculate total likes from Facebook posts
    facebook_likes = sum(post.get('likes', {}).get('summary', {}).get('total_count', 0) for post in facebook_data)

    # Pass data to the template
    return render(request, 'dashboard/analytics.html', {
        'twitter_likes': twitter_likes,
        'facebook_likes': facebook_likes
    })
