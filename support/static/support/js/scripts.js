document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.btn-success').forEach((button) => {
        button.addEventListener('click', () => {
            alert('Request marked as resolved!');
        });
    });
});
