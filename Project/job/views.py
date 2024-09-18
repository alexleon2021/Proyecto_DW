from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from .models import Job


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
    success_url = reverse_lazy('jobdescription')
    #Si el registro se crea de manera exitosa
    def get_success_url(self) -> str:
        return super().get_success_url()
    


class JobDetailView(DetailView):
    model = Job
    template_name = 'job/job_detail.html'

class EditJobView(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'job/job_edit.html'  
    success_url = reverse_lazy('job')


class DeleteJobView(DeleteView):
    model = Job
    success_url = reverse_lazy('job')  



class JobDescriptionView(TemplateView):
    template_name = 'job/jobdescription.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context