from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('requests/', views.list_service_requests, name='service_requests_list'),
    path('requests/<int:pk>/update/', views.update_service_request, name='update_service_request'),
]
