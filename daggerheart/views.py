from django.shortcuts import render


def home(request):
    """Daggerheart home page."""
    return render(request, 'daggerheart/home.html')
