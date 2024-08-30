from django import forms
from job.models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Programador JR'}),
            'mode': forms.Select(),
            'skills': forms.Select(),
            'position': forms.Select(),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Profesional con 1 año de experiencia'})
        }