from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test create a new user with an email successful."""
        email = 'krish@gmail.com'
        password = 'password1234'
        user = get_user_model().objects.create_user(
			email=email,
			password=password
		)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalize(self):
        """Test the email for new user is normalized."""
        email = "krish@GMAIL.com"
        user = get_user_model().objects.create_user(email, 'password1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test Creating user with no email raising error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
    
    def test_create_new_super_user(self):
        """Crating a new superuser."""
        user = get_user_model().objects.create_superuser(
            'superuser@gmail.com',
            'password1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_stuff)

