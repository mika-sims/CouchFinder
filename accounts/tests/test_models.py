from django.test import TestCase
from cities_light.models import Country, Region, City

from accounts.models import CustomUser, CustomUserProfile


class CustomUserModelTests(TestCase):
    # Setups for the tests
    def setUp(self):
        # Create a user
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
        self.assertEqual(self.user.REQUIRED_FIELDS, [
                         'first_name', 'last_name'])

    def test_str(self):
        # Test string representation of the CustomUser model
        self.assertEqual(str(self.user), 'Mikail Simsek')

    def test_verbose_name(self):
        # Test verbose name of the CustomUser model
        self.assertEqual(str(CustomUser._meta.verbose_name), 'user')

    def test_verbose_name_plural(self):
        # Test verbose name plural of the CustomUser model
        self.assertEqual(str(CustomUser._meta.verbose_name_plural), 'users')


class CustomUserProfileModelTests(TestCase):
    # Setup for the tests
    def setUp(self):
        # Create a user
        self.user = CustomUser.objects.create_user(
            first_name='Mikail',
            last_name='Simsek',
            email='mikailsimsek@mail.com',
            password='qwerty123'
        )

        # Create country, region and city
        country = Country.objects.create(name='Italy')
        region = Region.objects.create(name='Toscana', country=country)
        city = City.objects.create(name='Florence', region=region, country=country)

        # Create CustomUserProfile object
        CustomUserProfile.objects.create(
            user=self.user,
            profile_picture='profile_pictures/placeholder.png',
            bio='This is a test bio.',
            occupation='Full Stack Developer',
            profile_status='hosting',
            country=country,
            region=region,
            city=city
        )

    def test_str(self):
        # Test string representation of the CustomUserProfile model
        self.assertEqual(str(self.user.customuserprofile), 'Mikail Simsek')

    def test_get_location(self):
        # Test get_location method
        self.assertEqual(
            self.user.customuserprofile.get_location(), 'Florence, Toscana, Italy')

    def test_is_hosting(self):
        # Test is_hosting method
        self.assertTrue(self.user.customuserprofile.is_hosting())

    def test_is_travelling(self):
        # Test is_travelling method
        self.assertFalse(self.user.customuserprofile.is_travelling())

    def test_is_busy(self):
        # Test is_busy method
        self.assertFalse(self.user.customuserprofile.is_busy())
