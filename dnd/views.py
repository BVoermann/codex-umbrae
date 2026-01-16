from django.shortcuts import render
from dnd.information.context_dnd import context
from dnd.information.episodes_dnd import playlist_UH, playlist_UZ, playlist_GvD
from codexumbrae.auth_views import require_sessions_password


def home(request):
    """D&D home page."""

    return render(request, 'systems_home.html', context=context)

def campaign(request):
    """D&D campaign page."""
    return render(request, 'systems_campaign.html', context=context)

@require_sessions_password('dnd')
def sessions(request):
    """D&D sessions page."""
    campaign_id = request.GET.get('campaign')
    if campaign_id == 'Der-unermessliche-Zerfall':
        playlist_url = playlist_UZ
    elif campaign_id == 'Das-Geheimnis-von-Dyadan':
        playlist_url = playlist_GvD
    elif campaign_id == "Unbekannte-Heimat":
        playlist_url = playlist_UH
    else:
        playlist_url = []
    return render(request, 'systems_sessions.html', context={**context, 'playlist_url': playlist_url,})

def lore(request):
    """D&D lore page."""
    return render(request, 'systems_lore.html', context=context)

def characters(request):
    """D&D characters page."""
    return render(request, 'systems_characters.html', context=context)

def media(request):
    """D&D media page."""
    return render(request, 'systems_media.html', context=context)

def search(request):
    """D&D search page."""
    return render(request, 'systems_search.html', context=context)