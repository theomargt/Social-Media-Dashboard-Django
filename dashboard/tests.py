# ✅ Test User Authentication (Login & Dashboard Access)
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserAuthenticationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_login_valid_user(self):
        """Test if a valid user can log in successfully and is redirected"""
        response = self.client.post(reverse("login"), {"username": "testuser", "password": "testpass"})
        self.assertRedirects(response, reverse("dashboard"))  # ✅ Check correct redirect after login
        self.assertTrue(self.client.login(username="testuser", password="testpass"))  # ✅ Verify login session

    def test_dashboard_requires_login(self):
        """Test if the dashboard page requires authentication"""
        response = self.client.get(reverse("dashboard"))
        login_url = reverse("login") + "?next=" + reverse("dashboard")  # ✅ Dynamic redirect
        self.assertRedirects(response, login_url)  


# ✅ Test Social Media API Integration (Mocking API Call)
from django.test import TestCase
from unittest.mock import patch
from dashboard.utils import fetch_twitter_posts  # Import your function

class SocialMediaAPITests(TestCase):
    @patch("dashboard.utils.requests.get")  # ✅ Mock Twitter API call
    def test_fetch_twitter_posts(self, mock_get):
        """Test if Twitter API fetches posts correctly"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"tweets": ["Test Tweet 1", "Test Tweet 2"]}

        posts = fetch_twitter_posts("test_token")  # ✅ Call function with mocked API

        # ✅ Assertions
        self.assertEqual(len(posts["tweets"]), 2)  # Check correct number of tweets
        self.assertEqual(posts["tweets"][0], "Test Tweet 1")  # Check content
        self.assertEqual(posts["tweets"][1], "Test Tweet 2")
