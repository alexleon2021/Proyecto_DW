from django.urls import path
from .views import *
from Project import settings
from django.conf.urls.static import static

urlpatterns = [
    path('job/', ListJobsView.as_view(), name="job"),
    path('create/job/', CreateJobView.as_view(), name="createjob"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)