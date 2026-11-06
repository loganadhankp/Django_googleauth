from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class GoogleAuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@gmail.com",
            password="testpassword123",
            first_name="Test",
            last_name="User"
        )

    def test_home_page_unauthenticated(self):
        """Unauthenticated user sees Sign in with Google button"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign in with Google")
        self.assertContains(response, reverse("google_login"))
        self.assertContains(response, "You are not logged in.")

    def test_home_page_authenticated(self):
        """Authenticated user sees their name/email and logout option"""
        self.client.force_login(self.user)
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome, Test User!")
        self.assertContains(response, "testuser@gmail.com")
        self.assertContains(response, reverse("account_logout"))

    def test_urls_reverse_properly(self):
        """Allauth endpoints resolve properly"""
        self.assertEqual(reverse("home"), "/")
        self.assertEqual(reverse("account_login"), "/accounts/login/")
        self.assertEqual(reverse("account_logout"), "/accounts/logout/")
        self.assertEqual(reverse("google_login"), "/accounts/google/login/")
