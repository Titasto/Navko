from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView


# Create your views here.
class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'


