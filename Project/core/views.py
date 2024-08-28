from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import *
# Create your views here.



class CoreLoginView(LoginView):
    template_name = 'core/login.html'
    next_page = 'job'



