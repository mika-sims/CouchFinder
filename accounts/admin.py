from django.contrib import admin

from .models import CustomUser, CustomUserProfile

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'is_staff',
    )


@admin.register(CustomUserProfile)
class CustomUserProfileAdmin(admin.ModelAdmin):
    pass