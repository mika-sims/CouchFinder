from django.urls import path

from . import views


urlpatterns = [
    path('user_profile/', views.UserProfileView.as_view(), name='user_profile'),
]
