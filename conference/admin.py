from django.contrib import admin
from . import models

# Globally disable delete
admin.site.disable_action('delete_selected')

# Custom admin form for Speaker
@admin.register(models.Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic info', {
            'fields': (('first_name', 'last_name',), 'email', 'bio',)
        }),
        ('Social', {
            'classes': ('collapse',),
            'fields': ('facebook', 'instagram', 'twitter',)
        }),
    )


def approve_presentations(modeladmin, request, queryset):
    queryset.update(approved=True)
approve_presentations.short_description = 'Approve presentations'

def decline_presentations(modeladmin, request, queryset):
    queryset.update(approved=False)
decline_presentations.short_description = 'Decline presentations'

@admin.register(models.Presentation)
class PresentationAdmin(admin.ModelAdmin):
    fields = ('title', 'abstract', 'speaker', 'approved',)
    list_display = ('title', 'speaker', 'approved',)
    list_filter = ('approved', 'speaker',)
    actions = [approve_presentations, decline_presentations, ]


# Register your models here.
