from django.shortcuts import render


def home(request):
    """Vampire: The Masquerade home page."""
    return render(request, 'vampire/home.html')
