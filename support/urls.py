from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.support_dashboard, name='support_dashboard'),
    path('update_ticket/<int:ticket_id>/', views.update_ticket, name='update_ticket'),
]
