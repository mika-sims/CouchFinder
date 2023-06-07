from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserManagerTests(TestCase):
    # Setups for the tests
    def setUp(self):
        self.User = get_user_model()
        self.manager = self.User.objects
        self.first_name = 'Mikail'
        self.last_name = 'Simsek'
        self.email = 'mikailsimsek@mail.com'
        self.password = 'qwerty123'
        self.admin_email = "mikailsimsek@mail.com"
        self.admin_password = "qwerty123"

    def test_create_user(self):
        # Test creating a custom user
        user = self.manager.create_user(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            password=self.password,
        )
        self.assertEqual(user.email, self.email)
        self.assertEqual(user.first_name, self.first_name)
        self.assertEqual(user.last_name, self.last_name)
        self.assertTrue(user.check_password(self.password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

    def test_create_user_without_email(self):
        # Test creating a custom user without providing an email
        with self.assertRaises(ValueError):
            self.manager.create_user(
                email=None,
                password=self.password,
                first_name=self.first_name,
                last_name=self.last_name,
            )

    def test_create_user_without_password(self):
        # Test creating a custom user without providing a password
        with self.assertRaises(ValueError):
            self.manager.create_user(
                email=self.email,
                password=None,
                first_name=self.first_name,
                last_name=self.last_name,
            )

    def test_create_user_without_first_name(self):
        # Test creating a custom user without providing a first name
        with self.assertRaises(ValueError):
            self.manager.create_user(
                email=self.email,
                password=self.password,
                first_name=None,
                last_name=self.last_name,
            )

    def test_create_user_without_last_name(self):
        # Test creating a custom user without providing a last name
        with self.assertRaises(ValueError):
            self.manager.create_user(
                email=self.email,
                password=self.password,
                first_name=self.first_name,
                last_name=None,
            )

    def test_create_user_with_blank_first_name(self):
        # Test creating a custom user with a blank first name
        with self.assertRaises(ValueError):
            self.manager.create_user(
                email=self.email,
                password=self.password,
                first_name='',
                last_name=self.last_name,
            )

    def test_create_user_with_blank_last_name(self):
        # Test creating a custom user with a blank last name
        with self.assertRaises(ValueError):
            self.manager.create_user(
                email=self.email,
                password=self.password,
                first_name=self.first_name,
                last_name='',
            )

    def test_create_superuser(self):
        # Test creating a superuser
        user = self.manager.create_superuser(
            email=self.admin_email,
            first_name=self.first_name,
            last_name=self.last_name,
            password=self.admin_password,
        )
        self.assertEqual(user.email, self.admin_email)
        self.assertEqual(user.first_name, self.first_name)
        self.assertEqual(user.last_name, self.last_name)
        self.assertTrue(user.check_password(self.admin_password))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)

    def test_create_superuser_without_email(self):
        # Test creating a superuser without providing an email
        with self.assertRaises(ValueError):
            self.manager.create_superuser(
                email=None,
                password=self.admin_password,
                first_name=self.first_name,
                last_name=self.last_name,
            )

    def test_create_superuser_without_password(self):
        # Test creating a superuser without providing a password
        with self.assertRaises(ValueError):
            self.manager.create_superuser(
                email=self.admin_email,
                password=None,
                first_name=self.first_name,
                last_name=self.last_name,
            )

    def test_create_superuser_without_first_name(self):
        # Test creating a superuser without providing a first name
        with self.assertRaises(ValueError):
            self.manager.create_superuser(
                email=self.admin_email,
                password=self.admin_password,
                first_name=None,
                last_name=self.last_name,
            )
