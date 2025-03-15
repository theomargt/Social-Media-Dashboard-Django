from django.urls import path, include
import dashboard.views as views  # ✅ Import all views safely

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),  # ✅ Signup Page
    path("dashboard/", views.dashboard_view, name="dashboard"),  # ✅ Dashboard Page
    path("schedule_post/", views.schedule_post_view, name="schedule_post"),  # ✅ Schedule Post Page
    path("analytics/", views.analytics_view, name="analytics"),  # ✅ Analytics Page

    path("auth/", include("social_django.urls", namespace="social")),  # ✅ Social authentication URLs
]
