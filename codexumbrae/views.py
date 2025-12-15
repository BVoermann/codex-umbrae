from django.shortcuts import render


def index(request):
    """Main landing page with TTRPG system selection."""
    return render(request, 'index.html')
