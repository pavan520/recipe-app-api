from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating anew user with email is successful... """
        email = "test@londeonappdev.com"
        password = "Testpass123"
        user = get_user_model().objects().create_user(email=email,password=password)

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def text_new_user_email_normalized(self):
        """ tests the email for new user is normalized """
        email = 'test@newGMAIL.com'
        user = get_user_model().objects().create_user(email,'123')
        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """ Validates the email of new user if no email then it throws an error"""
        with self.assertRaises(ValueError):
            user = get_user_model().objects().create_user(None, '123')
