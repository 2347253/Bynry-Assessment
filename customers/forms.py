# customers/forms.py
from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'details', 'attachment']
        widgets = {
            'details': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter detailed description of the issue'}),
        }
