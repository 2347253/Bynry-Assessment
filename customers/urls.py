from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit_request/', views.submit_request, name='submit_request'),
    path('request_status/<int:request_id>/', views.request_status, name='request_status'),

    path('login/', views.login_view, name='login'),  # Or use your existing login view
    path('register/', views.register, name='register'),  # Or use your existing register view
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),



]
