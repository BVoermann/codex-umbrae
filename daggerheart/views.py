from django.shortcuts import render
from daggerheart.information.context_daggerheart import context
from codexumbrae.auth_views import require_sessions_password

def home(request):
    """Daggerheart home page."""

    return render(request, 'systems_home.html', context=context)

def campaign(request):
    """Daggerheart campaign page."""
    return render(request, 'systems_campaign.html', context=context)

@require_sessions_password('daggerheart')
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
