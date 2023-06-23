from django.http import JsonResponse
from django.utils import formats, timezone
from datetime import timedelta
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from allauth.account.views import PasswordResetFromKeyView, PasswordChangeView
from cities_light.models import Region, City


from .forms import UpdateUserProfileForm
from .models import CustomUserProfile


class UserProfileView(generic.TemplateView, LoginRequiredMixin):
    """
    View for the user profile page.
    """
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = CustomUserProfile.objects.get(user=self.request.user)
        date_joined = user_profile.user.date_joined
        last_login = user_profile.user.last_login

        formatted_date_joined = formats.date_format(date_joined, format='F j, Y')
        context['date_joined'] = formatted_date_joined

        time_elapsed = timezone.now() - last_login
        if time_elapsed < timedelta(hours=1):
            minutes = int(time_elapsed.total_seconds() // 60)
            formatted_last_login = f"{minutes} minute(s) ago"
        elif time_elapsed < timedelta(days=1):
            hours = int(time_elapsed.total_seconds() // 3600)
            formatted_last_login = f"{hours} hour(s) ago"
        else:
            days = int(time_elapsed.total_seconds() // 86400)
            formatted_last_login = f"{days} day(s) ago"

        context['last_login'] = formatted_last_login
        context['profile'] = user_profile
        return context


class UpdateUserProfileView(LoginRequiredMixin, generic.UpdateView):
    model = CustomUserProfile
    form_class = UpdateUserProfileForm
    template_name = 'update_profile.html'

    def get_success_url(self):
        return reverse_lazy('user_profile')

    def get_object(self, queryset=None):
        return self.request.user.customuserprofile

    def form_valid(self, form):
        response = super().form_valid(form)
        # Perform additional actions after a valid form submission if needed
        return response


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


class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):
    success_url = reverse_lazy('account_login')

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(view)


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('user_profile')

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(view)