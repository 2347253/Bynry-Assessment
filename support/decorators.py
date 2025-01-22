# support/decorators.py

from django.core.exceptions import PermissionDenied

def csr_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not getattr(request.user, 'is_csr', False):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view
