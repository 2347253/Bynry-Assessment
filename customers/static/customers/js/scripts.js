// customers/static/customers/js/scripts.js
document.addEventListener('DOMContentLoaded', () => {
    const statusBtns = document.querySelectorAll('.status-btn');
    statusBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const requestId = btn.dataset.requestId;
            const newStatus = btn.dataset.status;

            fetch(`/update_status/${requestId}/`, {
                method: 'POST',
                body: JSON.stringify({ status: newStatus }),
                headers: { 'Content-Type': 'application/json' }
            }).then(response => {
                if (response.ok) {
                    // Update status without reloading
                    btn.closest('tr').querySelector('.status-column').textContent = newStatus;
                } else {
                    alert("Failed to update status. Please try again.");
                }
            }).catch(error => {
                alert("An error occurred. Please try again.");
            });            
        });
    });
});
