from django.contrib import admin
from django.db.models import Count
from . import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'extension_name',
                    'email', 'permanent_address', 'current_address', 'municipality')
    list_per_page = 10


@admin.register(models.SALOG_Employee)
class SALOG_EmployeeAdmin(admin.ModelAdmin):
    list_display = ('person', 'designation', 'rank', 'date_started', 'status')
    list_per_page = 10


@admin.register(models.Researcher)
class ResearcherAdmin(admin.ModelAdmin):
    list_display = ('SALOG_employee', 'level', 'status')
    list_per_page = 10


@admin.register(models.Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ('title',  'number_of_researchers', 'description', 'status',
                    'date_started', 'date_ended', 'duration_in_months')
    list_per_page = 10

    @admin.display(ordering='researchers_count')
    def number_of_researchers(self, research):
        return research.researchers_count

    @admin.display(ordering='duration')
    def duration_in_months(self, research):
        return research.duration

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            researchers_count=Count('researcher')
        )

# *Research Details Entry and View is still under contraction


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status',
                    'date_started', 'date_ended', 'duration_in_months')
    list_per_page = 10

    @admin.display(ordering='duration')
    def duration_in_months(self, project):
        return project.duration

# SUBMITTED FILES TABLE
# *Setup Submitted Files and View User Interphase is still under construction


@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('project', 'research', 'name', 'description',
                    'activity_type', 'date_started', 'date_ended', 'duration_in_months')
    list_per_page = 10

    @admin.display(ordering='duration')
    def duration_in_months(self, activity):
        return activity.duration


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('project', 'research', 'name', 'details',
                    'category', 'date_posted', 'date_expired', 'status')
    list_per_page = 10
