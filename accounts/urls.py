from django.urls import path

from . import views


urlpatterns = [
    path('user_profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('update_profile/', views.UpdateProfileView.as_view(), name='update_profile'),
]
