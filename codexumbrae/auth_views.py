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
    # Check if already authenticated for this system
    if request.session.get(f'{system}_sessions_authenticated'):
        return redirect(f'/{system}/sessions')

    error_message = None

    if request.method == 'POST':
        password = request.POST.get('password', '')
        correct_password = settings.SYSTEM_PASSWORDS.get(system)

        if password == correct_password:
            # Set session flag for this system
            request.session[f'{system}_sessions_authenticated'] = True
            # Redirect to sessions page
            return redirect(f'/{system}/sessions')
        else:
            error_message = 'Incorrect password. Please try again.'

    # Render password entry form
    context = {
        'system': system,
        'system_title': system.upper() if system != 'daggerheart' else 'Daggerheart',
        'error_message': error_message,
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
                # Redirect to password entry page
                return redirect(f'/{system}/sessions/login')
            # User is authenticated, allow access
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
