from django.urls import path
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from . import views

urlpatterns = [
    path('user_profile/',
         views.UserProfileView.as_view(), name='user_profile'),
    path('update_profile/',
         views.UpdateUserProfileView.as_view(), name='update_profile'),
    path('password/reset/key/done/', views.CustomPasswordResetFromKeyView.as_view(),
         name='password_reset_from_key_done'),
]
