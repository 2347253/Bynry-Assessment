from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SupportTicket, SupportRepresentative
from .forms import TicketUpdateForm
from .decorators import csr_required  # Import csr_required decorator

@login_required
@csr_required
def support_dashboard(request):
    if not hasattr(request.user, 'supportrepresentative'):
        return redirect('home')  # Redirect non-support users
    tickets = SupportTicket.objects.all()
    return render(request, 'support/dashboard.html', {'tickets': tickets})

@login_required
def update_ticket(request, ticket_id):
    ticket = get_object_or_404(SupportTicket, id=ticket_id)
    if request.method == 'POST':
        form = TicketUpdateForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('support_dashboard')
    else:
        form = TicketUpdateForm(instance=ticket)
    return render(request, 'support/update_ticket.html', {'form': form, 'ticket': ticket})
