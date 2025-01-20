from django.shortcuts import render, get_object_or_404, redirect
from .models import ServiceRequest
from .forms import ServiceRequestUpdateForm
from django.contrib.auth.decorators import user_passes_test

def is_support_staff(user):
    return user.is_staff  # Assuming support staff are marked as `is_staff`

@user_passes_test(is_support_staff)
def list_service_requests(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'support/service_requests_list.html', {'requests': requests})

@user_passes_test(is_support_staff)
def update_service_request(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        form = ServiceRequestUpdateForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('support:service_requests_list')
    else:
        form = ServiceRequestUpdateForm(instance=service_request)
    return render(request, 'support/service_request_update.html', {'form': form, 'service_request': service_request})
