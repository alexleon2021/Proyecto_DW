from django.urls import path
from .views import *
from Project import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('job/', ListJobsView.as_view(), name="job"),
    path('create/job/', CreateJobView.as_view(), name="createjob"),
    path('job/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('job/<int:pk>/edit/', EditJobView.as_view(), name='edit_job'),
    path('job/<int:pk>/delete/', DeleteJobView.as_view(), name='delete_job'),
    path('jobdescription/<int:pk>/', JobDescriptionView.as_view(), name='jobdescription')

    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    