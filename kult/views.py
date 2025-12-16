from django.shortcuts import render


def home(request):
    """KULT home page."""
    context = {
        'stylesheet': 'css/kult.css',
        'site_title': 'KULT - Codex Umbrae',
        'title': 'KULT',
        'subtitle': "Divinity Lost",
        'welcome': 'Beyond the veil of reality lies the truth of our prison. '
                   'The illusion fractures. The metropolis bleeds.',
        'quote': '"We are but fragments of forgotten gods, wandering the labyrinth of lies."',
        'campaign_subtitle': 'Chronicles beyond sanity',
        'sessions_subtitle': 'Descents into the truth',
        'lore_subtitle': 'Forbidden knowledge',
        'characters_subtitle': 'Prisoners of the metropolis',
        'media_subtitle': 'Visions of the broken world',
        'search_subtitle': 'Seek what should not be found',
    }
    return render(request, 'systems_home.html', context=context)
