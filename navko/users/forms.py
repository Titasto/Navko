from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class UserProfileForm(forms.ModelForm):
    photo = forms.ImageField(required=False)
    username = forms.CharField(disabled=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-input'}))


    class Meta:
        model =get_user_model()
        fields = ['photo', 'username', 'email', 'first_name', 'last_name']

    labels = {
        'username': 'Username',
        'email': 'E-mail',
        'first_name': 'Fist name',
        'last_name': 'Last name'
    }

    widgets = {
        'first_name': forms.TextInput(attrs={'class': 'text-input'}),
        'last_name': forms.TextInput(attrs={'class': 'text-input'})
    }


class PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, label='Old password',
                                   widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                                                     "autofocus": True}))
    new_password1 = forms.CharField(max_length=50, label='New password',
                                   widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                                                     "autofocus": True}))
    new_password2 = forms.CharField(max_length=50, label='Repeat password',
                                   widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                                                     "autofocus": True}))

    class Meta:
        model = get_user_model()
        fields = ["old_password", "new_password1", "new_password2"]


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True, label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(max_length=50, required=True, label='E-mail')
    password1 = forms.CharField(max_length=50, required=True, label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'password-input'}))
    password2 = forms.CharField(max_length=50, required=True, label='Repeat password',
                                widget=forms.PasswordInput(attrs={'class': 'password-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email like this already exists')
        return email
