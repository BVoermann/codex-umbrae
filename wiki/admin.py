from django.contrib import admin
from .models import System, WikiEntry, WikiRevision

# Admin-Interface for managing systems/campaigns
@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
    ('Basic Information', {
        'fields': ('name', 'slug', 'description')
    }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('wiki_entries')


# Admin-Interface for managing Wiki Entries
@admin.register(WikiEntry)
class WikiEntryAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'system',
        'entry_type',
        'is_published',
        'is_spoiler',
        'views',
        'updated_at',
    ]
    list_filter = [
        'system',
        'entry_type',
        'is_published',
        'is_spoiler',
        'created_at',
        'updated_at',
    ]

    search_fields = ['title', 'content', 'summary', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['related_entries']  # UI-reasons

    date_hierarchy = 'created_at'

    fieldsets = (
        ('Basic Information', {
            'fields': ('system', 'title', 'slug', 'entry_type')
        }),
        ('Content', {
            'fields': ('summary', 'content', 'image'),
        }),
        ('Organization', {
            'fields': ('tags', 'related_entries'),
            'classes': ('collapse',),
        }),
        ('Settings', {
            'fields': ('is_published', 'is_spoiler'),
        }),
        ('Statistics', {
            'fields': ('views', 'created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ['views', 'created_at', 'updated_at']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    actions = ['publish_entries', 'unpublish_entries', 'mark_as_spoiler', 'unmark_as_spoiler']


    @admin.action(description='Publish selected entries')
    def publish_entries(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, f'{count} entries published.')

    @admin.action(description="Unpublish selected entries")
    def unpublish_entries(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(request, f'{count} entries unpublished.')

    @admin.action(description='Mark selected entries as spoiler')
    def mark_as_spoiler(self, request, queryset):
        count = queryset.update(is_spoiler=True)
        self.message_user(request, f'{count} entries marked as spoiled')

    @admin.action(description="Unmark selected entries as spoiler")
    def unmark_as_spoiler(self, request, queryset):
        count = queryset.update(is_spoiler=False)
        self.message_user(request, f'{count} entries marked as unspoiled.')


# Admin-Interface for reviewing edit history
@admin.register(WikiRevision)
class WikiRevisionAdmin(admin.ModelAdmin):
    list_display = ['entry', 'edited_by', 'edited_at', 'edit_summary']
    list_filter = ['edited_at', 'entry__system']
    search_fields = ['entry__title', 'content', 'edit_summary']
    readonly_fields = ['entry', 'content', 'summary', 'edited_by', 'edited_at']

    date_hierarchy = 'edited_at'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    fieldsets = (
        ('Revision Information', {
            'fields': ('entry', 'edited_by', 'edited_at', 'edit_summary'),
        }),
        ('Content at this revision', {
            'fields': ('summary', 'content'),
            'classes': ('collapse',),
        }),
    )

# Optional: Inline for showing revisions on WikiEntry edit page
class WikiRevisionInline(admin.TabularInline):
    model = WikiRevision
    extra = 0
    readonly_fields = ['edited_by', 'edited_at', 'edit_summary']
    fields = ['edited_at', 'edited_by', 'edited_summary']

    def has_add_permission(self, request, obj=None):
        return False


# Uncomment to add revision history to WikiEntry admin page:
# WikiEntryAdmin.inlines = [WikiRevisionInline]