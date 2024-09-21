from django.forms import BaseModelForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from .models import Job, Mode, Skills, Company, Position, City  # Cambié Address y Skill
from job.forms import JobForm
from django.views.decorators.csrf import csrf_exempt
import json

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
        context['job'] = self.get_Job()  # Asegúrate de llamar a la función
        return context

def add_new_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        description = data.get('description')
        company = Company.objects.create(
            description=description
        )
        return JsonResponse({'message': 'Item created successfully'}, status=200)
    
from django.http import JsonResponse
from django.shortcuts import render
from .models import Company  # O el modelo que estés usando

def add_company(request):
    if request.method == 'POST':
        # Procesar la creación de la empresa
        name = request.POST.get('name')
        # Aquí agregar lógica para crear la empresa, posiblemente con una imagen
        
        # Retornar el nuevo campo como HTML
        new_field_html = render_to_string('job/company_field.html', {'company': name})
        return JsonResponse({'new_field': new_field_html})

