from django.shortcuts import render


def home(request):
    """Daggerheart home page."""
    context = {
        'stylesheet': 'css/daggerheart.css',
        'site_title': 'Daggerheart - Codex Umbrae',
        'title': 'Daggerheart',
        'subtitle': "Where Hope and Fear Collide",
        'welcome': 'In a world of magic and peril, heroes rise to face impossible odds. '
                   'Every roll of the dice brings both triumph and tribulation.',
        'quote': '"Hope is the dagger, fear is the heart."',
        'campaign_subtitle': 'Epic tales of adventure',
        'sessions_subtitle': 'Chronicles of heroic deeds',
        'lore_subtitle': 'Legends and mythology',
        'characters_subtitle': 'Champions of the realm',
        'media_subtitle': 'Visions of wonder',
        'search_subtitle': 'Quest through the archives',
    }
    return render(request, 'systems_home.html', context=context)
