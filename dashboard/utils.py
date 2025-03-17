import os
import requests

# Load Twitter Bearer Token from environment variables
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")

def get_twitter_posts():
    """
    Fetches the latest tweets from the authenticated user's Twitter account.
    Uses OAuth 2.0 Bearer Token for authentication.
    """
    url = "https://api.twitter.com/2/users/me/tweets"  # Twitter API v2 endpoint
    headers = {
        "Authorization": f"Bearer {TWITTER_BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Returns tweets in JSON format
    else:
        return {"error": response.json(), "status_code": response.status_code}

def get_facebook_posts():
    """
    Fetches the latest posts from the authenticated user's Facebook account.
    Uses the Facebook Graph API with an access token.
    """
    url = f"https://graph.facebook.com/me/posts?access_token={FACEBOOK_ACCESS_TOKEN}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # Returns Facebook posts in JSON format
    else:
        return {"error": response.json(), "status_code": response.status_code}
