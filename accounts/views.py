from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import forms
from . import models


class UserProfileView(TemplateView, LoginRequiredMixin):
    """
    View for the user profile page.
    """
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = models.CustomUserProfile.objects.get(
            user=self.request.user)
        return context