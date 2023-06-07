from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user manager that provides methods for creating and managing users.
    """

    def create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        Creates and saves a new user with the given fields.
        """
        if not first_name:
            raise ValueError("The First Name field must be set")
        if not last_name:
            raise ValueError("The Last Name field must be set")
        if not email:
            raise ValueError("The Email field must be set")
        if not password:
            raise ValueError("The Password field must be set")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        """
        Creates and saves a new superuser with the given fields.
        """
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(email, first_name, last_name, password, **extra_fields)
