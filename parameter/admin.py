from django.contrib import admin
from django.db.models import Count
from . import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'extension_name',
                    'email', 'permanent_address', 'current_address', 'municipality')
    list_per_page = 10
    search_fields = ['first_name__icontains', 'middle_name__icontains',
                     'last_name__icontains', 'extension_name__icontains']


@admin.register(models.SALOG_Employee)
class SALOG_EmployeeAdmin(admin.ModelAdmin):
    list_display = ('person', 'designation', 'rank', 'date_started', 'status')
    list_per_page = 10


@admin.register(models.Researcher)
class ResearcherAdmin(admin.ModelAdmin):
    list_display = ('SALOG_employee', 'level', 'status')
    list_per_page = 10


class ResearchResearcherInline(admin.StackedInline):
    model = models.ResearchResearcher
    extra = 0
    min_num = 1
    verbose_name = 'Researcher'
    verbose_name_plural = 'Researchers'


@admin.register(models.Research)
class ResearchAdmin(admin.ModelAdmin):
    inlines = [ResearchResearcherInline]
    list_display = ('title', 'author', 'abstract', 'status',
                    'date_started', 'date_ended', 'duration_in_months')
    list_per_page = 10

    def author(self, research):
        researchers = []
        separator = ' | '
        queryset = research.research_researcher.all()
        for researcher in queryset:
            researchers.append(str(researcher))
        return separator.join(researchers)

    @admin.display(ordering='description')
    def abstract(self, research):
        description = str(research.description)
        if description.__len__() > 100:
            description = description[:100]
            return description.rstrip() + '...'
        return description

    @admin.display(ordering='duration')
    def duration_in_months(self, research):
        return research.duration

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('research_researcher__researcher__SALOG_employee__person')

# *Research Details Entry and View is still under contraction


class ProjectEmployeeInline(admin.StackedInline):
    model = models.ProjectEmployee
    extra = 0
    min_num = 1
    verbose_name = 'Employee'
    verbose_name_plural = 'Employees'


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectEmployeeInline]
    list_display = ('title', 'SALOG_Employees', 'description', 'status',
                    'date_started', 'date_ended', 'duration_in_months')
    list_per_page = 10

    def SALOG_Employees(self, project):
        employees = []
        separator = ' | '
        queryset = project.project_employee.all()
        for employee in queryset:
            employees.append(str(employee))
        return separator.join(employees)

    def description(self, project):
        description = project.project_description
        if description.__len__() > 100:
            description = description[:100]
            return description.rstrip() + '...'
        return description

    @admin.display(ordering='duration')
    def duration_in_months(self, project):
        return project.duration

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('project_employee__employee__person')

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
