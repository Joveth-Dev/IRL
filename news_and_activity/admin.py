from django.contrib import admin
from . import models


@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    autocomplete_fields = ['project', 'research']
    list_display = ('project', 'research', 'name', 'activity_description',
                    'activity_type', 'date_started', 'date_ended', 'duration_in_hours')
    list_filter = ['activity_type', 'date_started', 'date_ended']
    list_per_page = 10
    list_select_related = ['project', 'research']
    ordering = ['-date_started']
    search_fields = ['project__title__icontains', 'research__title__icontains',
                     'name__icontains', 'description__icontains']

    @admin.display(ordering='description', description='description')
    def activity_description(self, activity: models.Activity):
        description = activity.description
        if len(description) < 50:
            description = description[:50]
            return description.rstrip() + '...'
        return description


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    autocomplete_fields = ['project', 'research']
    list_display = ['project', 'research', 'name', 'news_details',
                    'category', 'date_posted', 'date_expired', 'status']
    list_filter = ['category', 'date_posted', 'date_expired', 'status']
    list_per_page = 10
    list_select_related = ['project', 'research']
    ordering = ['-date_posted']
    search_fields = ['project__title__icontains',
                     'research__title__icontains', 'name__icontains', 'details__icontains']

    @admin.display(ordering='details', description='details')
    def news_details(self, news: models.News):
        details = news.details
        if len(details) < 50:
            details = details[:50]
            return details.rstrip() + '...'
        return details
