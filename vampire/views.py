from django.shortcuts import render
import requests
import yt_dlp
from vampire.information.context_vampire import context
from vampire.information.episodes_vampire import (
    playlist_BBNA, playlist_BBNC, playlist_TBNC,
    playlist_id_BBNA, playlist_id_BBNC, playlist_id_TBNC,
    transcripts_first_part_BBNC, transcripts_first_part_BBNA, transcripts_first_part_TBNC,
    git_tree_BBNC, git_tree_BBNA, git_tree_TBNC
)
from codexumbrae.auth_views import require_sessions_password

def home(request):
    """Vampire home page."""

    return render(request, 'systems_home.html', context=context)

def campaign(request):
    """Vampire campaign page."""
    prefix = "https://www.youtube.com/playlist?list="
    real_playlist_BBNC = prefix + playlist_id_BBNC
    real_playlist_BBNA = prefix + playlist_id_BBNA
    real_playlist_TBNC = prefix + playlist_id_TBNC
    with yt_dlp.YoutubeDL({"quiet": True, "extract_flat": True}) as ydl:
        BBNC_info = ydl.extract_info(real_playlist_BBNC, download=False)
        BBNA_info = ydl.extract_info(real_playlist_BBNA, download=False)
        TBNC_info = ydl.extract_info(real_playlist_TBNC, download=False)
        played_sessions_BBNC = len(BBNC_info["entries"])
        played_sessions_BBNA = len(BBNA_info["entries"])
        played_sessions_TBNC = len(TBNC_info["entries"]) - 2

    return render(request, 'systems_campaign.html', context={
        **context,
        'played_sessions_BBNC': played_sessions_BBNC,
        'played_sessions_BBNA': played_sessions_BBNA,
        'played_sessions_TBNC': played_sessions_TBNC,
    })

@require_sessions_password('vampire')
def sessions(request):
    """Vampire sessions page."""
    campaign_id = request.GET.get('campaign')
    if campaign_id == 'Berlin-By-Night-Camarilla':
        playlist_url = playlist_BBNC
        playlist_id = playlist_id_BBNC
        transcript_url = transcripts_first_part_BBNC
        response = requests.get(git_tree_BBNC)
    elif campaign_id == 'Berlin-By-Night-Anarchs':
        playlist_url = playlist_BBNA
        playlist_id = playlist_id_BBNA
        transcript_url = transcripts_first_part_BBNA
        response = requests.get(git_tree_BBNA)
    elif campaign_id == "Turin-By-Night-Camarilla":
        playlist_url = playlist_TBNC
        playlist_id = playlist_id_TBNC
        transcript_url = transcripts_first_part_TBNC
        response = requests.get(git_tree_TBNC)
    else:
        playlist_url = []
        playlist_id = ""
        transcript_url = ""
        episode_range = range(1)
        response = None

    if response:
        data = response.json()
        files = [item for item in data['tree'] if item['type'] == 'blob']
        episode_range = range(1, len(files))

    return render(request, 'vampire/sessions.html', context={
        **context,
        'playlist_url': playlist_url,
        'playlist_id': playlist_id,
        'transcript_url': transcript_url,
        'episode_range': episode_range,
    })

def lore(request):
    """Vampire lore page."""
    return render(request, 'systems_lore.html', context=context)

def characters(request):
    """Vampire characters page."""
    return render(request, 'systems_characters.html', context=context)
