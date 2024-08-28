from django.contrib import admin
from django.urls import path
from .views import *
from Project import settings

urlpatterns = [
    path('', CoreLoginView.as_view(), name="login"),
]


