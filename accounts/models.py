from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from cities_light.models import Country, Region, City

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model extending the AbstractBaseUser class.
    """

    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(
        max_length=254, unique=True, blank=False, null=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class CustomUserProfile(models.Model):
    """
    Custom user profile model.
    """

    PROFILE_STATUS = (
        ('hosting', 'Hosting'),
        ('travelling', 'Travelling'),
        ('busy', 'Busy'),
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_pictures', default='placeholder.png')
    bio = models.TextField(blank=True, default='')
    occupation = models.CharField(max_length=250, blank=True, default='')
    profile_status = models.CharField(
        max_length=10, choices=PROFILE_STATUS, default='busy')
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey(
        Region, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def get_location(self):
        return f'{self.city.name}, {self.region.name}, {self.country.name}'
    
    def is_hosting(self):
        return self.profile_status == 'hosting'
    
    def is_travelling(self):
        return self.profile_status == 'travelling'
    
    def is_busy(self):
        return self.profile_status == 'busy'