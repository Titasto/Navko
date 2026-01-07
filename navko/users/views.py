from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from users.forms import LoginUserForm, UserProfileForm, UserRegistrationForm, PasswordChange


# Create your views here.
class Login(LoginView):
    template_name = 'users/login.html'
    extra_context = {'title': 'Login'}
    form_class = LoginUserForm


class UpdateUserProfile(UpdateView):
    model = get_user_model()
    template_name = 'users/user_profile.html'
    form_class = UserProfileForm
    success_url = '/'
    extra_context = {'title': 'Profile'}

    def get_object(self, queryset = ...):
        return self.request.user


class UserRegistrationView(CreateView):
    model = get_user_model()
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    form_class = UserRegistrationForm


class ChangePasswordView(PasswordChangeView):
    template_name = 'users/password_change_form.html'
    success_url = reverse_lazy('users:user_profile')
    form_class = PasswordChange