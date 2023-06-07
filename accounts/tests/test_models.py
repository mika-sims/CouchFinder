from django.test import TestCase
from django.utils import timezone

from accounts.models import CustomUser


class CustomUserModelTests(TestCase):
    # Setups for the tests
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            first_name='Mikail',
            last_name='Simsek',
            email='mikailsimsek@mail.com',
            password='qwerty123'
        )
    
    def test_objects(self):
        # Test the objects manager
        self.assertTrue(self.user)
    
    def test_username_field(self):
        # Test the username field
        self.assertEqual(self.user.USERNAME_FIELD, 'email')
    
    def test_required_fields(self):
        # Test the required fields
        self.assertEqual(self.user.REQUIRED_FIELDS, ['first_name', 'last_name'])
        
    def test_str(self):
        # Test string representation of the CustomUser model
        self.assertEqual(str(self.user), 'Mikail Simsek')
    
    def test_verbose_name(self):
        # Test verbose name of the CustomUser model
        self.assertEqual(str(CustomUser._meta.verbose_name), 'user')
    
    def test_verbose_name_plural(self):
        # Test verbose name plural of the CustomUser model
        self.assertEqual(str(CustomUser._meta.verbose_name_plural), 'users')
    