from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import (SignupForm, LoginForm)
from cities_light.models import Country, Region, City

from .models import CustomUserProfile


class CustomSignUpForm(SignupForm):

    first_name = forms.CharField(max_length=30, label='First Name',
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name',
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    remember_me = forms.BooleanField(required=False, label='Remember Me',
                                     widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        for field_name in [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]:
            self.fields[field_name].label = False

    def clean_email(self):
        # Check if the email address is already verified
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email, emailaddress__verified=False).exists():
            raise forms.ValidationError(
                'An account with this email address has been created but is not yet verified. '
                'Please check your email for the verification link.'
            )
        return email

    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class CustomLoginForm(LoginForm):

    remember_me = forms.BooleanField(required=False, label='Remember Me',
                                     widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget = forms.TextInput(attrs={
            'placeholder': 'Email*',
        })
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Password*',
        })

        for field_name in [
            'login',
            'password',
        ]:
            self.fields[field_name].label = False

    def login(self, *args, **kwargs):
        return super(CustomLoginForm, self).login(*args, **kwargs)


class UpdateUserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(
        required=False, widget=forms.FileInput(attrs={'class': 'form-horizontal'}))
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea(
        attrs={'rows': 6, 'placeholder': 'Write something detailed about yourself'}))
    occupation = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'form-horizontal', 'placeholder': 'What do you do?'}))
    status = forms.ChoiceField(choices=CustomUserProfile.PROFILE_STATUS, widget=forms.Select(
        attrs={'class': 'form-horizontal'}))
    country = forms.ModelChoiceField(queryset=Country.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-horizontal'}))
    region = forms.ModelChoiceField(queryset=Region.objects.all(
    ), required=False, widget=forms.Select(attrs={'class': 'form-horizontal'}))
    city = forms.ModelChoiceField(queryset=City.objects.all(
    ), required=False, widget=forms.Select(attrs={'class': 'form-horizontal'}))

    class Meta:
        model = CustomUserProfile
        fields = ('profile_picture', 'bio', 'occupation',
                  'profile_status', 'country', 'region', 'city')

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.profile_picture = self.cleaned_data.get('profile_picture')
        profile.bio = self.cleaned_data.get('bio')
        profile.occupation = self.cleaned_data.get('occupation')
        profile.profile_status = self.cleaned_data.get('profile_status')
        profile.country = self.cleaned_data.get('country')
        profile.region = self.cleaned_data.get('region')
        profile.city = self.cleaned_data.get('city')
        if commit:
            profile.save()
        return profile
