from django.urls import path
from .views import *
from Project import settings

urlpatterns = [
    path('job/', ListJobsView.as_view(), name="job"),
]
