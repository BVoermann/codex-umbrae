from django.shortcuts import render
from vampire.information.context_vampire import context

def home(request):
    """Daggerheart home page."""

    return render(request, 'systems_home.html', context=context)

def campaign(request):
    """Daggerheart campaign page."""
    return render(request, 'systems_campaign.html', context=context)

def sessions(request):
    """Daggerheart sessions page."""
    return render(request, 'systems_sessions.html', context=context)

def lore(request):
    """Daggerheart lore page."""
    return render(request, 'systems_lore.html', context=context)

def characters(request):
    """Daggerheart characters page."""
    return render(request, 'systems_characters.html', context=context)

def media(request):
    """Daggerheart media page."""
    return render(request, 'systems_media.html', context=context)

def search(request):
    """Daggerheart search page."""
    return render(request, 'systems_search.html', context=context)
