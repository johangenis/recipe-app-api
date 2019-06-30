from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email="sample_user@johangenis.com", password="password"):
    """Creare sample user."""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = "test@johangenis.com"
        password = "Test123"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if the email for a new user is normalized."""
        email = "test@JOHANGENIS.COM"
        user = get_user_model().objects.create_user(email, "Test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating new user without email raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "Test123")

    def test_new_superuser(self):
        """Test creating a new superuser."""
        user = get_user_model().objects.create_superuser(
            "test@johangenis.com", "Test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test tag string representation."""
        tag = models.Tag.objects.create(user=sample_user(), name="Vegan")

        self.assertEqual(str(tag), tag.name)
