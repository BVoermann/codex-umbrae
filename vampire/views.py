from django.shortcuts import render


def home(request):
    """Vampire: The Masquerade home page."""
    return render(request, 'systems_home.html')
