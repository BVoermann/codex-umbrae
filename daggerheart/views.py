from django.shortcuts import render
from daggerheart.information.context_daggerheart import context
from daggerheart.information.episodes_daggerheart import playlist_KdS, transcripts_first_part_KdS
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
    campaign_id = request.GET.get('campaign')
    if campaign_id == 'Kinder-des-Schleiers':
        playlist_url = playlist_KdS
        transcript_url = transcripts_first_part_KdS
        episode_range = range(1, 4 + 1)
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
    """Daggerheart lore page."""
    return render(request, 'systems_lore.html', context=context)

def characters(request):
    """Daggerheart characters page."""
    return render(request, 'systems_characters.html', context=context)
