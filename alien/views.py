from django.shortcuts import render
import requests
from alien.information.context_alien import context
from alien.information.episodes_alien import playlist_SdG
from codexumbrae.auth_views import require_sessions_password

def home(request):
    """Alien home page."""

    return render(request, 'systems_home.html', context=context)

def campaign(request):
    """Alien campaign page."""
    return render(request, 'systems_campaign.html', context=context)

@require_sessions_password('alien')
def sessions(request):
    """Alien sessions page."""
    campaign_id = request.GET.get('campaign')
    if campaign_id == 'Streitwagen-der-Goetter':
        playlist_url = playlist_SdG
    else:
        playlist_url = []

    return render(request, 'systems_sessions.html', context={
        **context,
        'playlist_url': playlist_url,
    })


def lore(request):
    """Alien lore page."""
    return render(request, 'systems_lore.html', context=context)

def characters(request):
    """Alien characters page."""
    return render(request, 'systems_characters.html', context=context)
