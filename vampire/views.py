from django.shortcuts import render
from vampire.information.context_vampire import context
from vampire.information.episodes_vampire import (
    playlist_BBNA, playlist_BBNC, transcripts_first_part_BBNC, transcripts_first_part_BBNA)
from codexumbrae.auth_views import require_sessions_password

def home(request):
    """Vampire home page."""

    return render(request, 'systems_home.html', context=context)

def campaign(request):
    """Vampire campaign page."""
    return render(request, 'systems_campaign.html', context=context)

@require_sessions_password('vampire')
def sessions(request):
    """Vampire sessions page."""
    campaign_id = request.GET.get('campaign')
    if campaign_id == 'Berlin-By-Night-Camarilla':
        playlist_url = playlist_BBNC
        transcript_url = transcripts_first_part_BBNC
        episode_range = range(1, 14 + 1)
    elif campaign_id == 'Berlin-By-Night-Anarchs':
        playlist_url = playlist_BBNA
        transcript_url = transcripts_first_part_BBNA
        episode_range = range(1, 6 + 1)
    else:
        playlist_url = []
        transcript_url = ""
        episode_range = range(1)
    return render(request, 'systems_sessions.html', context={
        **context,
        'playlist_url': playlist_url,
        'transcript_url': transcript_url,
        'episode_range': episode_range,
    })

def lore(request):
    """Vampire lore page."""
    return render(request, 'systems_lore.html', context=context)

def characters(request):
    """Vampire characters page."""
    return render(request, 'systems_characters.html', context=context)
