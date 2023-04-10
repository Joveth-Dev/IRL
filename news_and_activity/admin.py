from datetime import datetime
from django.contrib import admin
from . import models


@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    actions = ['post', 'remove_post']
    autocomplete_fields = ['project', 'research']
    fields = ['project', 'research', 'name', 'description', 'activity_type',
              'date_started', 'date_ended', 'duration_in_hours', 'is_posted']
    list_display = ['project', 'research', 'name', 'activity_description', 'activity_type',
                    'date_started', 'date_ended', 'duration_in_hours', 'date_posted', 'is_posted']
    list_filter = ['activity_type', 'date_started', 'date_ended']
    list_per_page = 10
    list_select_related = ['project', 'research']
    ordering = ['-date_started']
    search_fields = ['project__title__icontains', 'research__title__icontains',
                     'name__icontains', 'description__icontains']

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        if obj.is_posted:
            obj.date_posted = datetime.now().date()
        if not obj.is_posted:
            obj.date_posted = None
        return super().save_model(request, obj, form, change)

    def get_fields(self, request, obj=None):
        fields = list(self.fields)
        if obj and obj.is_posted:
            fields.append('date_posted')
        return fields

    @admin.display(ordering='description', description='description')
    def activity_description(self, activity: models.Activity):
        description = activity.description
        if len(description) < 50:
            description = description[:50]
            return description.rstrip() + '...'
        return description

    @admin.action(description='Post selected activities')
    def post(self, request, queryset):
        updated_count = queryset.update(
            is_posted=True,
            date_posted=datetime.now().date(),
        )
        self.message_user(
            request,
            f'{updated_count} activities were successfully posted!',
            "success"
        )

    @admin.action(description='Remove selected activities from posts')
    def remove_post(self, request, queryset):
        updated_count = queryset.update(
            is_posted=False,
            date_posted=None,
        )
        self.message_user(
            request,
            f'{updated_count} activities were removed from posts!',
            "error"
        )


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    actions = ['post', 'remove_post']
    autocomplete_fields = ['project', 'research']
    fields = ['project', 'research', 'name', 'details',
              'category', 'date_expired', 'status', 'is_posted']
    list_display = ['project', 'research', 'name', 'news_details',
                    'category', 'date_posted', 'date_expired', 'status', 'date_posted', 'is_posted']
    list_filter = ['category', 'date_posted', 'date_expired', 'status']
    list_per_page = 10
    list_select_related = ['project', 'research']
    ordering = ['-date_posted']
    search_fields = ['project__title__icontains',
                     'research__title__icontains', 'name__icontains', 'details__icontains']

    def save_model(self, request, obj, form, change):
        if obj.is_posted:
            obj.date_posted = datetime.now().date()
        if not obj.is_posted:
            obj.date_posted = None
        return super().save_model(request, obj, form, change)

    def get_fields(self, request, obj=None):
        fields = list(self.fields)
        if obj and obj.is_posted:
            fields.append('date_posted')
        return fields

    def has_delete_permission(self, request, obj=None):
        return False

    @admin.display(ordering='details', description='details')
    def news_details(self, news: models.News):
        details = news.details
        if len(details) < 50:
            details = details[:50]
            return details.rstrip() + '...'
        return details

    @admin.action(description='Post selected news')
    def post(self, request, queryset):
        updated_count = queryset.update(
            is_posted=True,
            date_posted=datetime.now().date(),
        )
        self.message_user(
            request,
            f'{updated_count} news were successfully posted!',
            "success"
        )

    @admin.action(description='Remove selected news from posts')
    def remove_post(self, request, queryset):
        updated_count = queryset.update(
            is_posted=False,
            date_posted=None,
        )
        self.message_user(
            request,
            f'{updated_count} news were removed from posts!',
            "error"
        )
