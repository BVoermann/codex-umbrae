from django.shortcuts import render
import requests
from alien.information.context_alien import context
from alien.information.episodes_alien import playlist_SdG, transcripts_first_part_SdG, git_tree_SdG
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
        transcript_url = transcripts_first_part_SdG
        response = requests.get(git_tree_SdG)
    else:
        playlist_url = []
        transcript_url = ""
        episode_range = range(1)
        response = None

    if response:
        data = response.json()
        files = [item for item in data['tree'] if item['type'] == 'blob']
        episode_range = range(1, len(files))

    return render(request, 'systems_sessions.html', context={
        **context,
        'playlist_url': playlist_url,
        'transcript_url': transcript_url,
        'episode_range': episode_range,
    })


def lore(request):
    """Alien lore page."""
    return render(request, 'systems_lore.html', context=context)

def characters(request):
    """Alien characters page."""
    return render(request, 'systems_characters.html', context=context)
