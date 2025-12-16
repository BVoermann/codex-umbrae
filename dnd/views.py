from django.shortcuts import render
from dnd.information.context_dnd import context


def home(request):
    """D&D home page."""

    return render(request, 'systems_home.html', context=context)


def campaign(request):
    """D&D campaign page."""
    return render(request, 'systems_campaign.html', context=context)

def sessions(request):
    """D&D sessions page."""
    return render(request, 'systems_sessions.html', context=context)

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