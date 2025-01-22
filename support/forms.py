from django import forms
from .models import SupportTicket

class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['notes']
        widgets = {
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add notes...'}),
        }
