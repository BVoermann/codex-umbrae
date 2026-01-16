from django.shortcuts import render
from kult.information.context_kult import context
from kult.information.episodes_kult import playlist_OOD
from codexumbrae.auth_views import require_sessions_password

def home(request):
    """KULT home page."""

    return render(request, 'systems_home.html', context=context)

def campaign(request):
    """KULT campaign page."""
    return render(request, 'systems_campaign.html', context=context)

@require_sessions_password('kult')
def sessions(request):
    """KULT sessions page."""
    campaign_id = request.GET.get('campaign')
    if campaign_id == 'Ordo-Orbis-Dei':
        playlist_url = playlist_OOD
    else:
        playlist_url = []
    return render(request, 'systems_sessions.html', context={**context, 'playlist_url': playlist_url,})

def lore(request):
    """KULT lore page."""
    return render(request, 'systems_lore.html', context=context)

def characters(request):
    """KULT characters page."""
    return render(request, 'systems_characters.html', context=context)

def media(request):
    """KULT media page."""
    return render(request, 'systems_media.html', context=context)

def search(request):
    """KULT search page."""
    return render(request, 'systems_search.html', context=context)
