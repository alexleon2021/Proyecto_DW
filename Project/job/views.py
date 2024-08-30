from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from job.forms import JobForm
from .models import *
# Create your views here.


class ListJobsView(ListView):
    model = Job
    template_name = 'job/listJob.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["background"] = "bg-slate-100"	
        return context
    
class CreateJobView(CreateView):
    template_name = "job/formJob.html"
    model = Job
    form_class = JobForm
    success_url = reverse_lazy('job')
    
