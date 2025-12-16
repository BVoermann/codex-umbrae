from django.shortcuts import render


def home(request):
    """Vampire: The Masquerade home page."""
    context = {
        'stylesheet': 'css/vampire.css',
        'site_title': 'Vampire: The Masquerade - Codex Umbrae',
        'title': 'Vampire: The Masquerade',
        'subtitle': "Enter the World of Darkness",
        'welcome': 'Welcome to the shadows, where immortal predators walk among mortals, '
                   'bound by ancient traditions and cursed with an insatiable thirst.',
        'quote': '"A Beast I am, lest a Beast I become."',
        'campaign_subtitle': 'Chronicles of darkness',
        'sessions_subtitle': 'Tales from the endless night',
        'lore_subtitle': 'Secrets of the Kindred',
        'characters_subtitle': 'Children of Caine',
        'media_subtitle': 'Images from the shadows',
        'search_subtitle': 'Hunt through the archives',
    }
    return render(request, 'systems_home.html', context=context)
