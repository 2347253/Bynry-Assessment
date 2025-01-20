from django.shortcuts import render, redirect
from .models import Customer, ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden

@login_required
def service_request_form(request):
    try:
        customer = request.user.customer
    except Customer.DoesNotExist:
        return HttpResponseForbidden("You must be a customer to submit a service request.")

    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = customer
            service_request.save()
            messages.success(request, "Service request submitted successfully.")
            return redirect('customers:request_status')
    else:
        form = ServiceRequestForm()

    return render(request, 'customers/service_request_form.html', {'form': form})

@login_required
def request_status(request):
    try:
        customer = request.user.customer
    except Customer.DoesNotExist:
        return HttpResponseForbidden("You must be a customer to view service requests.")

    requests = ServiceRequest.objects.filter(customer=customer)
    return render(request, 'customers/request_status.html', {'requests': requests})
