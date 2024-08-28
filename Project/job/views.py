from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.


class ListJobsView(ListView):
    model = Job
    template_name = 'job/listJob.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["background"] = "bg-slate-100"	
        return context
    
