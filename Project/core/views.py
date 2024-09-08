from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import *
# Create your views here.



class CoreLoginView(LoginView):
    template_name = 'core/login.html'
    next_page = 'job'


class RegisterView(TemplateView):
    template_name = 'core/register.html'

