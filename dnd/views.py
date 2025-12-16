from django.shortcuts import render


def home(request):
    """D&D home page."""
    context = {
        'stylesheet': 'css/dnd.css',
        'site_title': 'D&D - Codex Umbrae',
        'title': 'Dungeons & Dragons',
        'subtitle': "The World's Greatest Roleplaying Game",
        'welcome': 'Gather your party and venture forth into realms of magic, mystery, and endless adventure. '
                   'Heroes are forged in the fires of battle and the bonds of friendship.',
        'quote': '"The story is yours to tell."',
        'campaign_subtitle': 'Legendary quests await',
        'sessions_subtitle': 'Tales of valor and glory',
        'lore_subtitle': 'Ancient knowledge',
        'characters_subtitle': 'Heroes of legend',
        'media_subtitle': 'Treasures and artifacts',
        'search_subtitle': 'Explore the archives',
    }
    return render(request, 'dnd/home.html', context=context)
