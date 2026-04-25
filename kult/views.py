from django.shortcuts import render
from kult.information.context_kult import context
from kult.information.episodes_kult import playlist_OOD, playlist_id_OOD
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
        playlist_id = playlist_id_OOD
    else:
        playlist_url = []
        playlist_id = ""
    return render(request, 'kult/sessions.html', context={**context, 'playlist_url': playlist_url, 'playlist_id': playlist_id})

def lore(request):
    """KULT lore page."""
    return render(request, 'systems_lore.html', context=context)

def characters(request):
    """KULT characters page."""
    return render(request, 'systems_characters.html', context=context)
