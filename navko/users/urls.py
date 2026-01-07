from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),

    path('user_profile', views.UpdateUserProfile.as_view(), name='user_profile'),

    path('password_change/', views.ChangePasswordView.as_view(), name='password_change'),

    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset_form.html',
                                                            email_template_name='users/password_reset_email.html',
                                                            success_url=reverse_lazy('users:password_reset_done')),
                                                            name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
                                                            name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                                                      success_url=reverse_lazy('users:password_reset_complete')),
                                                            name='password_reset_confirm'),
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
                                                            name='password_reset_complete')
]