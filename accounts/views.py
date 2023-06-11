from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from . import forms
from . import models


class UserProfileView(generic.TemplateView, LoginRequiredMixin):
    """
    View for the user profile page.
    """
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = models.CustomUserProfile.objects.get(
            user=self.request.user)
        return context


@method_decorator(login_required, name='dispatch')
class EditUserProfileView(generic.UpdateView):
    model = models.CustomUserProfile
    form_class = forms.UpdateUserProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('user_profile')
    
    def get_object(self):
        return models.CustomUserProfile.objects.get(user=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('user_profile')