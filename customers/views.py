from django.shortcuts import render, redirect, get_object_or_404
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import ServiceRequest  # Ensure this import exists



# Homepage view
def home(request):
    return render(request, 'customers/home.html')

# Service request submission view
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)  
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user  # Link to logged-in user
            service_request.save()
            return redirect('request_status', request_id=service_request.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'customers/submit_request.html', {'form': form})

# View to track request status
def request_status(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id, customer=request.user)
    return render(request, 'customers/request_status.html', {'service_request': service_request})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after login
    else:
        form = AuthenticationForm()
    return render(request, 'customers/login.html', {'form': form})

# Register view
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after successful registration
            return redirect('dashboard')  # Redirect to the dashboard page (you can create it later)
    else:
        form = UserRegistrationForm()
    return render(request, 'customers/register.html', {'form': form})

def dashboard(request):
    # Fetch all requests associated with the logged-in user
    user_requests = ServiceRequest.objects.filter(customer=request.user)
    
    # If no requests, redirect to the request submission page
    if not user_requests:
        return redirect('submit_request')  # Assuming 'submit_request' is the name of the URL for the request form
    
    # Otherwise, render the dashboard with the user's requests
    return render(request, 'customers/dashboard.html', {'requests': user_requests})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout