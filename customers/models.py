from django.db import models
from django.contrib.auth.models import User  # Assuming you are using Django's built-in User model

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relating to the Django user model
    address = models.TextField()  # Address or any other customer-specific details
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.user.username

class ServiceRequest(models.Model):
    service_type_choices = [
        ('Gas Leak', 'Gas Leak'),
        ('Maintenance', 'Maintenance'),
        ('Installation', 'Installation'),
        ('Billing Issue', 'Billing Issue'),
        ('Other', 'Other'),
    ]

    service_type = models.CharField(max_length=20, choices=service_type_choices)
    details = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_service_requests')  # Unique related_name
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    attachment = models.FileField(upload_to='service_requests/', null=True, blank=True)

    def __str__(self):
        return f"Request {self.id} - {self.service_type}"
