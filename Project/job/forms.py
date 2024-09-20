from django import forms
from job.models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['description']
        labels = {
            'title': 'Titulo de la Oferta',
            'mode': 'Modalidad',
            'skills': 'Aptitudes y Habilidades',
            'company': 'Empresa',
            'address': 'Lugar de Trabajo',
            'position': 'Cargo',
            'description': 'Descripcion'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg', 
                'placeholder': 'Programador JR'
            }),
            'mode': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg'
            }),
            'company': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg'
            }),
            'address': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg'
            }),
            'skills': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg'
            }),
            'position': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg', 
                'placeholder': 'Profesional con 1 año de experiencia',
                'rows': 4
            })
        }
        

