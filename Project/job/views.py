from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
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
    #Si el registro se crea de manera exitosa
    def get_success_url(self) -> str:
        return reverse_lazy('jobdescription', args=[self.object.pk])
    
    


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

    def get_jobId(self, **kwargs):
        jobId = self.kwargs.get('pk')
        return jobId
    
    def get_Job(self):
        jobId = self.get_jobId()
        job = Job.objects.get(pk=jobId)
        return job
    
    def post(self, request, pk):
        job = self.get_Job()
        descripcion = request.POST.get("description")
        if descripcion:
            job.description = descripcion
            job.save()
            return redirect('job')
        return

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = self.get_Job
        return context
    