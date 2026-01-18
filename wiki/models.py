from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

class System(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the system")
    slug = models.SlugField(unique=True, help_text="URL-friendly abbreviation of the name")
    description = models.TextField(blank=True, help_text="Brief description of the system")

    class Meta:
        ordering = ['name']
        verbose_name = "System"
        verbose_name_plural = "Systems"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wiki:wiki_home', kwargs={'system_slug': self.slug})


class WikiEntry(models.Model):

    ENTRY_TYPES = [
        ('location', 'Ort'),
        ('npc', 'NPC'),
        ('player_character', 'Spielercharakter'),
        ('item', 'Gegenstand'),
        ('faction', 'Fraktion'),
        ('event', 'Historisches Ereignis'),
        ('creature', 'Kreatur'),
        ('deity', 'Gottheit'),
        ('spell', 'Zauber'),
        ('other', 'Anderes'),
    ]

    system = models.ForeignKey(
        System,
        on_delete=models.CASCADE,
        related_name='wiki_entries',
        help_text="Which system this entry belongs to"
    )

    title = models.CharField(max_length=200, help_text="Entry title")

    slug = models.SlugField(
        max_length=200,
        blank=True,
        help_text="URL-friendly abbreviation of the title"
    )

    entry_type = models.Charfield(
        max_length=30,
        choices=ENTRY_TYPES,
        help_text="Type of entry"
    )

    # Content
    summary = models.TextField(
        blank=True,
        help_text="Short summary of the entry"
    )
    content = models.TextField(
        help_text="Main content of the entry"
    )

    # Optional metadata
    image = models.ImageField(
        upload_to="wiki/",
        blank=True,
        null=True,
        help_text="Optional image for this entry"
    )
    tags = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional, comma-separated tags for this entry"
    )

    # Related entries, optional
    related_entries = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        help_text="Link to other related wiki entries"
    )

    # Tracking
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="User who created this entry"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0, help_text="How many views this entry has")

    # Visibility
    is_published = models.BooleanField(
        default=True,
        help_text="Whether this entry is visible to viewers"
    )
    is_spoiler = models.BooleanField(
        default=False,
        help_text="Marks this as spoiler and hides it from viewers"
    )

    class Meta:
        unique_together = ['system', 'slug']
        ordering = ['title']
        verbose_name = "Wiki Entry"
        verbose_name_plural = "Wiki Entries"
        indexes = [
            models.Index(fields=['system', 'entry_type']),
            models.Index(fields=['title']),
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return f"{self.title} ({self.system.name}"

    # auto-generates slug from title, if no slug is given
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def increment_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_tags_list(self):
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',')]
        return []

class WikiRevision(models.Model):
    entry = models.ForeignKey(
        WikiEntry,
        on_delete=models.CASCADE,
        related_name='revisions',
    )
    content = models.TextField(help_text="Content at this revision")
    summary = models.TextField(blank=True, help_text="Short summary at this revision")
    edited_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    edited_at = models.DateTimeField(auto_now_add=True)
    edit_summary = models.CharField(
        max_length=200,
        blank=True,
        help_text="Brief description on made changes"
    )

    class Meta:
        ordering = ['-edited_at']
        verbose_name = "Wiki Revision"
        verbose_name_plural = "Wiki Revisions"

    def __str__(self):
        return f"{self.entry.title} - {self.edited_at.strftime('%H:%M %d.%m.%Y')}"

