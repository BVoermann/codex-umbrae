from django.shortcuts import render


def home(request):
    """KULT home page."""
    return render(request, 'systems_home.html')
