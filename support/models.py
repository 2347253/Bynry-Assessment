from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from customers.models import ServiceRequest

class SupportRepresentative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username

class SupportTicket(models.Model):
    service_request = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE, related_name="support_ticket")
    assigned_to = models.ForeignKey(SupportRepresentative, on_delete=models.SET_NULL, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ticket for {self.service_request.customer.username} - {self.service_request.request_type}"
