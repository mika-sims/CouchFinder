from django.http import JsonResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from cities_light.models import Region, City

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


class UpdateProfileView(LoginRequiredMixin, FormView):
    """
    View for the update profile page.
    """
    template_name = 'update_profile.html'
    form_class = forms.UpdateUserProfileForm
    success_url = 'user_profile'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user.customuserprofile
        return kwargs

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)


def get_regions(request):
    country_id = request.GET.get('country_id')
    regions = Region.objects.filter(country_id=country_id)
    data = {
        'regions': [{'id': region.id, 'name': region.name} for region in regions]
    }
    return JsonResponse(data)


def get_cities(request):
    region_id = request.GET.get('region_id')
    cities = City.objects.filter(region_id=region_id)
    data = {
        'cities': [{'id': city.id, 'name': city.name} for city in cities]
    }
    return JsonResponse(data)
