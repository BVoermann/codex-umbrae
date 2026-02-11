from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import System, WikiEntry, WikiRevision


# Main Wiki Index Page
def wiki_home(request, system_slug):
    system = get_object_or_404(System, slug=system_slug)

    # Get Statistics
    total_entries = WikiEntry.objects.filter(
        system=system,
        is_published=True
    ).count()

    # Get entry counts by type
    entry_counts = WikiEntry.objects.filter(
        system=system,
        is_published=True
    ).values('entry_type').annotate(count=Count('id'))

    # Recent entries
    recent_entries = WikiEntry.objects.filter(
        system=system,
        is_published=True
    ).order_by('-created_at')[:10]

    # Popular entries
    popular_entries = WikiEntry.objects.filter(
        system=system,
        is_published=True
    ).order_by('-views')[:5]

    entry_counts_dict = {item['entry_type']: item['count'] for item in entry_counts}
    entry_types_with_counts = [
        {'key': key, 'label': label, 'count': entry_counts_dict[key]}
        for key, label in WikiEntry.ENTRY_TYPES
        if entry_counts_dict.get(key, 0) > 0
    ]

    context = {
        'system': system,
        'total_entries': total_entries,
        'entry_counts': entry_counts,
        'entry_types_with_counts': entry_types_with_counts,
        'recent_entries': recent_entries,
        'popular_entries': popular_entries,
        'entry_types': WikiEntry.ENTRY_TYPES,
    }
    return render(request, 'wiki/wiki_home.html', context)

# List all wiki entries with ordering and sorting options
def wiki_list(request, system_slug):
    system = get_object_or_404(System, slug=system_slug)

    entries = WikiEntry.objects.filter(
        system=system,
        is_published=True
    )

    # Filter by type
    entry_type = request.GET.get('type')
    if entry_type:
        entries = entries.filter(entry_type=entry_type)

    # Filter by tag
    tag = request.GET.get('tag')
    if tag:
        entries = entries.filter(tags__icontains=tag)

    # Sort options
    sort = request.GET.get('sort', 'title')
    if sort == 'recent':
        entries = entries.order_by('-created_at')
    elif sort == 'updated':
        entries = entries.order_by('-updated_at')
    elif sort == 'popular':
        entries = entries.order_by('-views')
    else:
        entries = entries.order_by('title')

    context = {
        'system': system,
        'entries': entries,
        'entry_types': WikiEntry.ENTRY_TYPES,
        'selected_type': entry_type,
        'selected_tag': tag,
        'selected_sort': sort,
    }
    return render(request, 'wiki/wiki_list.html', context)

# Display a single wiki entry
def wiki_detail(request, system_slug, entry_slug):
    system = get_object_or_404(System, slug=system_slug)
    entry = get_object_or_404(
        WikiEntry,
        system=system,
        slug=entry_slug,
        is_published=True
    )

    entry.increment_views()

    # Get related (manually picked) and similar (automatically picked) entries
    related = entry.related_entries.filter(is_published=True)[:5]

    similar = WikiEntry.objects.filter(
        system=system,
        entry_type=entry.entry_type,
        is_published=True
    ).exclude(id=entry.id).order_by('?')[:5]

    context = {
        'system': system,
        'entry': entry,
        'related_entries': related,
        'similar_entries': similar,
    }
    return render(request, 'wiki/wiki_detail.html', context)

# Search wiki entries within a system
def wiki_search(request, system_slug):
    system = get_object_or_404(System, slug=system_slug)
    query = request.GET.get('q').strip()

    results = []
    result_count = 0

    if query:
        results = WikiEntry.objects.filter(
            system=system,
            is_published=True
        ).filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(summary__icontains=query) |
            Q(tags__icontains=query)
        ).distinct().order_by('-views')

        result_count = results.count()

    context = {
        'system': system,
        'query': query,
        'results': results,
        'result_count': result_count,
        'entry_types': WikiEntry.ENTRY_TYPES,
    }
    return render(request, 'wiki/wiki_search.html', context)


# Show all entries of a specific type (NPC, etc.)
def wiki_by_type(request, system_slug, entry_type):
    system = get_object_or_404(System, slug=system_slug)

    valid_types = [t[0] for t in WikiEntry.ENTRY_TYPES]
    if entry_type not in valid_types:
        return redirect('wiki:wiki_home', system_slug=system_slug)

    entries = WikiEntry.objects.filter(
        system=system,
        entry_type=entry_type,
        is_published=True
    ).order_by('title')

    type_display = dict(WikiEntry.ENTRY_TYPES).get(entry_type, entry_type)
    entry_counts_dict = {item['entry_type']: item['count'] for item in entry_counts}

    context = {
        'system': system,
        'entries': entries,
        'entry_type': type_display,
        'type_display': type_display,
        'entry_counts_dict': entry_counts_dict,
    }
    return render(request, 'wiki/wiki_by_type.html', context)

# Create a new wiki entry
@login_required
def wiki_create(request, system_slug):
    system = get_object_or_404(System, slug=system_slug)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        entry_type = request.POST.get('entry_type')
        summary = request.POST.get('summary', '').strip()
        content = request.POST.get('content', '').strip()
        tags = request.POST.get('tags', '').strip()

        # basic validation
        if not title or not entry_type or not content:
            messages.error(request, 'Title, Type, and Content are required.')
            return render(request, 'wiki/wiki_create.html', {
                'system': system,
                'entry_type': WikiEntry.ENTRY_TYPES,
            })

        # create entry
        try:
            entry = WikiEntry.objects.create(
                system=system,
                title=title,
                entry_type=entry_type,
                summary=summary,
                content=content,
                tags=tags,
                created_by=request.user,
            )

            messages.success(request, f'Wiki entry "{title}" created successfully.')
            return redirect(entry.get_absolute_url())
        except Exception as e:
            messages.error(request, f'Error creating entry: {str(e)}')

    context = {
        'system': system,
        'entry_types': WikiEntry.ENTRY_TYPES,
    }
    return render(request, 'wiki/wiki_create.html', context)


# Edit an existing wiki
@login_required
def wiki_edit(request, system_slug, entry_slug):
    system = get_object_or_404(System, slug=system_slug)
    entry = get_object_or_404(WikiEntry, system =system, slug=entry_slug)

    if request.method == "POST":
        # save previous version to revisions
        WikiRevision.objects.create(
            entry=entry,
            content=entry.content,
            summary=entry.summary,
            edited_by=request.user,
            edit_summary=request.POST.get('edit_summary', ''),
        )

        # update entry
        entry.title = request.POST.get('title', entry.title)
        entry.entry_type = request.POST.get('entry_type', entry.entry_type)
        entry.summary = request.POST.get('summary', entry.summary)
        entry.content = request.POST.get('content', entry.content)
        entry.tags = request.POST.get('tags', entry.tags)
        entry.save()

        messages.success(request, f'"{entry.title}" updated successfully!')
        return redirect(entry.get_absolute_url())

    context = {
        'system': system,
        'entry': entry,
        'entry_types': WikiEntry.ENTRY_TYPES,
    }
    return render(request, 'wiki/wiki_edit.html', context)
