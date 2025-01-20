# customers/urls.py
from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('request_form/', views.service_request_form, name='service_request_form'),
    path('request_status/', views.request_status, name='request_status'),
]
