from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('installation', 'Installation'),
        ('repair', 'Repair'),
        ('maintenance', 'Maintenance'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='Pending')  # Example status field
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)  # Optional attachment field
    is_csr = models.BooleanField(default=False)  # New field to flag CSR

    def __str__(self):
        return f"{self.request_type} - {self.status}"
