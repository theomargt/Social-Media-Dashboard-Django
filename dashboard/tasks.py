from celery import shared_task
import requests
import os

@shared_task
def scheduled_post(message):
    """
    This Celery task posts a message to Twitter and Facebook.
    """
    # Twitter API Request
    twitter_url = "https://api.twitter.com/2/tweets"
    twitter_headers = {"Authorization": f"Bearer {os.getenv('TWITTER_API_KEY')}"}
    twitter_data = {"text": message}
    requests.post(twitter_url, headers=twitter_headers, json=twitter_data)

    # Facebook API Request
    facebook_url = f"https://graph.facebook.com/me/feed?message={message}&access_token={os.getenv('FACEBOOK_ACCESS_TOKEN')}"
    requests.post(facebook_url)
