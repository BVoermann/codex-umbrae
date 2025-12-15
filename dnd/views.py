from django.shortcuts import render


def home(request):
    """D&D home page."""
    return render(request, 'dnd/home.html')
