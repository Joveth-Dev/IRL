from datetime import datetime
from django.contrib import admin
from django.db.models import OuterRef, Subquery
from django.db.models.functions import Concat
from django.utils.html import format_html
from . import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'extension_name',
                    'email', 'permanent_address', 'current_address', 'municipality')
    list_per_page = 10
    ordering = ['last_name']
    search_fields = ['first_name__icontains', 'middle_name__icontains',
                     'last_name__icontains', 'extension_name__icontains']

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ['name', 'sex', 'agency_or_address']
    list_filter = ['sex']
    list_per_page = 10
    ordering = ['name']
    search_fields = ['name__icontains', 'agency_or_address']

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.Program)
class ProgramAdmin(admin.ModelAdmin):
    actions = ['post', 'remove_post']
    fields = ['title', 'coordinator', 'executive_summary', 'is_posted']
    list_display = ['title', 'coordinator',
                    'program_executive_summary', 'date_posted', 'is_posted']
    list_filter = ['date_posted', 'is_posted']
    list_per_page = 10
    list_select_related = ['coordinator']
    ordering = ['coordinator']
    search_fields = ['title__icontains',
                     'coordinator__name__icontains', 'executive_summary__icontains']

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj: models.Program, form, change):
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

    @admin.display(ordering='executive_summary', description='executive summary')
    def program_executive_summary(self, program: models.Program):
        executive_summary = program.executive_summary
        if executive_summary.__len__() > 100:
            executive_summary = executive_summary[:100]
            return executive_summary.rstrip() + '...'
        return executive_summary

    @admin.action(description='Post selected program/s')
    def post(self, request, queryset):
        updated_count = queryset.update(
            is_posted=True,
            date_posted=datetime.now().date(),
        )
        self.message_user(
            request,
            f'{updated_count} programs were successfully posted!',
            "success"
        )

    @admin.action(description='Remove selected program/s from posts')
    def remove_post(self, request, queryset):
        updated_count = queryset.update(
            is_posted=False,
            date_posted=None,
        )
        self.message_user(
            request,
            f'{updated_count} programs were removed from posts!',
            "error"
        )


@admin.register(models.IRL_Employee)
class IRL_EmployeeAdmin(admin.ModelAdmin):
    list_display = ('person', 'designation', 'rank', 'date_started', 'status')
    list_filter = ['status', 'rank', 'date_started', 'designation']
    list_per_page = 10
    list_select_related = ['person']
    ordering = ['-date_started']
    search_fields = ['person__first_name__icontains',
                     'person__middle_name__icontains', 'person__last_name__icontains', 'designation__icontains']

    def has_delete_permission(self, request, obj=None):
        return False


class AgencyInline(admin.StackedInline):
    extra = 2
    fields = ['logo_thumbnail', 'logo', 'type', 'name']
    max_num = 2
    min_num = 2
    model = models.Agency
    readonly_fields = ['logo_thumbnail']

    def logo_thumbnail(self, agency: models.Agency):
        return format_html(f'<img src="{agency.logo.url}" alt="logo.img" class="linkage_partner_list">')


class IRLEmployeeInline(admin.TabularInline):
    extra = 0
    min_num = 1
    model = models.Project.IRL_employees.through
    verbose_name = 'IRL Employee'
    verbose_name_plural = 'IRL Employees'


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    actions = ['post', 'remove_post']
    autocomplete_fields = ['program']
    fields = ['program', 'title', 'project_summary', 'sampling_site', 'sampling_site_image',
              'references', 'status', 'date_started', 'date_ended', 'duration', 'is_posted']
    inlines = [IRLEmployeeInline, AgencyInline]
    list_display = ['title', 'project_program', 'IRL_Employees', 'project_summary_description',
                    'status', 'date_started', 'date_ended', 'duration_in_months', 'date_posted', 'is_posted']
    list_filter = ['status', 'date_started', 'date_ended']
    list_per_page = 10
    ordering = ['-date_started']
    search_fields = ['title__icontains', 'program__title__icontains',
                     'project_description__icontains']

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

    def get_queryset(self, request):
        queryset = super().get_queryset(request). \
            select_related('program'). \
            prefetch_related('IRL_employees__person')
        first_employee = models.Project.objects. \
            filter(IRL_employees=OuterRef('pk')). \
            order_by('-pk'). \
            values('IRL_employees__person__first_name')[:1]
        return queryset.annotate(first_employee=Subquery(first_employee))

    @admin.display(ordering='program', description='program')
    def project_program(self, project: models.Project):
        if project.program is not None:
            program = project.program.title
            if len(program) < 50:
                program = program[:50]
                return program.rsplit() + '...'
            return program
        return 'None'

    @admin.display(ordering='-first_employee')
    def IRL_Employees(self, project: models.Project):
        return format_html('<br>'.join([str(employee) for employee in project.IRL_employees.all()]))

    @admin.display(ordering='project_summary', description='project summary')
    def project_summary_description(self, project):
        description = project.project_summary
        if description.__len__() > 50:
            description = description[:50]
            return description.rstrip() + '...'
        return description

    @admin.display(ordering='duration')
    def duration_in_months(self, project):
        return project.duration

    @admin.action(description='Post selected project/s')
    def post(self, request, queryset):
        updated_count = queryset.update(
            is_posted=True,
            date_posted=datetime.now().date(),
        )
        self.message_user(
            request,
            f'{updated_count} projects were successfully posted!',
            "success"
        )

    @admin.action(description='Remove selected project/s from posts')
    def remove_post(self, request, queryset):
        updated_count = queryset.update(
            is_posted=False,
            date_posted=None,
        )
        self.message_user(
            request,
            f'{updated_count} projects were removed from posts!',
            "error"
        )

    class Media:
        css = {
            'all': ['parameter/styles.css']
        }

# SUBMITTED FILES TABLE
# *Setup Submitted Files and View User Interphase is still under construction


@admin.register(models.Researcher)
class ResearcherAdmin(admin.ModelAdmin):
    list_display = ['IRL_employee', 'level', 'status']
    list_filter = ['status', 'level']
    list_per_page = 10
    ordering = ['IRL_employee']
    search_fields = ['IRL_employee__person__first_name__icontains',
                     'IRL_employee__person__middle_name__icontains', 'IRL_employee__person__last_name__icontains']

    def has_delete_permission(self, request, obj=None):
        return False


class LinkagePartnerInline(admin.TabularInline):
    extra = 0
    min_num = 1
    model = models.Research.linkage_partners.through
    verbose_name = 'Linkage Partner'
    verbose_name_plural = 'Linkage Partners'


class EquipmentInline(admin.TabularInline):
    extra = 0
    model = models.Research.equipment.through
    verbose_name = 'Equipment'
    verbose_name_plural = 'Equipments'


class ResearcherInline(admin.TabularInline):
    extra = 0
    min_num = 1
    model = models.Research.researchers.through
    verbose_name = 'Researcher'
    verbose_name_plural = 'Researchers'


@admin.register(models.Research)
class ResearchAdmin(admin.ModelAdmin):
    actions = ['post', 'remove_post']
    autocomplete_fields = ['project', 'equipment']
    fields = ['project', 'title', 'description', 'status',
              'date_started', 'date_ended', 'duration', 'is_posted']
    inlines = [ResearcherInline, EquipmentInline, LinkagePartnerInline]
    list_display = ['title', 'research_project', 'research_researchers', 'abstract', 'status',
                    'date_started', 'date_ended', 'duration_in_months', 'date_posted', 'is_posted']
    list_filter = ['project', 'status', 'date_started', 'date_ended']
    list_per_page = 10
    ordering = ['-date_started']
    search_fields = ['title__icontains', 'project__title__icontains',
                     'researchers__IRL_employee__person__first_name__icontains',
                     'researchers__IRL_employee__person__middle_name__icontains',
                     'researchers__IRL_employee__person__last_name__icontains']

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

    def get_queryset(self, request):
        queryset = super().get_queryset(request). \
            select_related('project',). \
            prefetch_related(
                'researchers__IRL_employee__person', 'equipment', 'linkage_partners')
        first_researcher = models.Research.objects. \
            filter(researchers=OuterRef('pk')). \
            values('researchers__IRL_employee__person__first_name')[:1]
        return queryset.annotate(first_researcher=Subquery(first_researcher))

    @admin.display(ordering='program', description='program')
    def research_project(self, research: models.Research):
        if research.project is not None:
            project = research.project.title
            if len(project) < 50:
                project = project[:50]
                return project.rstrip() + '...'
            return project
        return 'None'

    @admin.display(ordering='first_researcher', description='researchers')
    def research_researchers(self, research: models.Research):
        return format_html('<br>'.join([str(researcher) for researcher in research.researchers.all()]))

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

    @admin.action(description='Post selected research/es')
    def post(self, request, queryset):
        updated_count = queryset.update(
            is_posted=True,
            date_posted=datetime.now().date(),
        )
        self.message_user(
            request,
            f'{updated_count} researches were successfully posted!',
            "success"
        )

    @admin.action(description='Remove selected research/es from posts')
    def remove_post(self, request, queryset):
        updated_count = queryset.update(
            is_posted=False,
            date_posted=None,
        )
        self.message_user(
            request,
            f'{updated_count} researches were removed from posts!',
            "error"
        )

# *Research Details Entry and View is still under contraction

    class Media:
        css = {
            'all': ['parameter/styles.css']
        }


@admin.register(models.LinkagePartner)
class LinkagePartnerAdmin(admin.ModelAdmin):
    fields = ['logo', 'name', 'description', 'status']
    list_display = ['linkage_partner_logo', 'name', 'description', 'status']
    list_filter = ['status']
    list_per_page = 10
    ordering = ['name']
    readonly_fields = ['linkage_partner_logo']
    search_fields = ['name__icontains', 'description__icontains']

    def has_delete_permission(self, request, obj=None):
        return False

    def get_fields(self, request, obj=None):
        fields = list(self.fields)
        if obj:
            fields.insert(0, 'linkage_partner_logo')
        return fields

    @admin.display(description='logo thumbnail')
    def linkage_partner_logo(self, linkage_partners: models.LinkagePartner):
        return format_html(f'<img src="{linkage_partners.logo.url}" class="linkage_partner_list">')

    class Media:
        css = {
            'all': ['parameter/styles.css']
        }


@admin.register(models.Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'image']
    list_display = ['name', 'description', 'image', 'image_thumbnail']
    list_per_page = 10
    ordering = ['name']
    readonly_fields = ['thumbnail', 'image_thumbnail']
    search_fields = ['name__icontains', 'description__icontains']

    def has_delete_permission(self, request, obj=None):
        return False

    def get_fields(self, request, obj=None):
        fields = list(self.fields)
        if obj:
            fields.append('thumbnail')
        return fields

    def thumbnail(self, equiment):
        return format_html(f'<img src="{equiment.image.url}" class="equipment">')

    def image_thumbnail(self, equiment):
        return format_html(f'<img src="{equiment.image.url}" class="equipment_list">')

    class Media:
        css = {
            'all': ['parameter/styles.css']
        }
