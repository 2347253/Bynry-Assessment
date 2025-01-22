from django import forms
from .models import ServiceRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'attachment']

    request_type = forms.ChoiceField(
        choices=ServiceRequest.REQUEST_TYPES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form-control'  # Add class for styling
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        # Add classes to the username and password fields
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm your password'})

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class CSRLoginForm(AuthenticationForm):
    csr_passphrase = forms.CharField(
        max_length=50, 
        required=False, 
        widget=forms.PasswordInput(attrs={'placeholder': 'CSR Passphrase (optional)'})
    )

    def clean(self):
        cleaned_data = super().clean()
        csr_passphrase = cleaned_data.get('csr_passphrase')
        if csr_passphrase:
            from django.conf import settings
            if not check_password(csr_passphrase, settings.CSR_HASH):
                raise forms.ValidationError("Invalid CSR passphrase.")
        return cleaned_data
