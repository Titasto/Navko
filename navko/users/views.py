from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import UpdateView

from users.forms import LoginUserForm, UserProfileForm


# Create your views here.
class Login(LoginView):
    template_name = 'users/login.html'
    extra_context = {'title': 'Login'}
    form_class = LoginUserForm


class UpdateUserProfile(UpdateView):
    model = get_user_model()
    template_name = 'users/user_profile'
    form_class = UserProfileForm
    success_url = '/'
    extra_context = {'title': 'Prodile'}

    def get_object(self, queryset = ...):
        return self.request.user