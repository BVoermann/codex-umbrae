from django.shortcuts import render, redirect
from django.conf import settings
from functools import wraps


def sessions_password_check(request, system):
    """
    View to handle password authentication for system sessions pages.

    Args:
        request: Django request object
        system: The system name (dnd, vampire, kult, daggerheart)
    """
    # Get the 'next' URL (where to redirect after login)
    next_url = request.GET.get('next', f'/{system}/sessions')

    # Check if already authenticated for this system
    if request.session.get(f'{system}_sessions_authenticated'):
        return redirect(next_url)

    error_message = None

    if request.method == 'POST':
        password = request.POST.get('password', '')
        correct_password = settings.SYSTEM_PASSWORDS.get(system)
        # Get next_url from the hidden form field
        next_url = request.POST.get('next', f'/{system}/sessions')

        if password == correct_password:
            # Set session flag for this system
            request.session[f'{system}_sessions_authenticated'] = True
            # Redirect to the original page (with query params preserved)
            return redirect(next_url)
        else:
            error_message = 'Incorrect password. Please try again.'

    # Render password entry form
    context = {
        'system': system,
        'system_title': system.upper() if system != 'daggerheart' else 'Daggerheart',
        'error_message': error_message,
        'next_url': next_url,
    }
    return render(request, 'sessions_password.html', context)


def require_sessions_password(system):
    """
    Decorator to protect sessions views with password authentication.

    Args:
        system: The system name (dnd, vampire, kult, daggerheart)

    Usage:
        @require_sessions_password('dnd')
        def sessions(request):
            ...
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # Check if user is authenticated for this system's sessions
            if not request.session.get(f'{system}_sessions_authenticated'):
                # Build the full current URL (path + query string)
                current_url = request.get_full_path()
                # Redirect to password entry page with 'next' parameter
                return redirect(f'/{system}/sessions/login?next={current_url}')
            # User is authenticated, allow access
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
