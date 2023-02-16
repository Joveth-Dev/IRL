from rest_framework import serializers
from . import models


class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Research
        fields = ['id', 'title', 'researcher_id', 'description', 'status',
                  'date_started', 'date_ended', 'duration']

    researcher_id = serializers.SerializerMethodField()

    def get_researcher_id(self, research: models.Research):
        researchers = []
        queryset = research.research_researcher.all()
        for research in queryset:
            researchers.append(
                research.researcher.id)
            # researcher.researcher.SALOG_employee.person.get_full_name())
        return researchers


# ============= This classes can/will be displayed in the researchers/ endpoint =============
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'extension_name',
                  'permanent_address', 'current_address', 'municipality', 'email']


class SALOG_EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SALOG_Employee
        fields = ['id', 'designation', 'rank',
                  'date_started', 'status', 'person']  #

    person = PersonSerializer()
# =======================================================================================


class ResearcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Researcher
        fields = ['id', 'researcher_level',
                  'researcher_status', 'SALOG_employee']  #

    SALOG_employee = SALOG_EmployeeSerializer()
    researcher_level = serializers.SerializerMethodField()
    researcher_status = serializers.SerializerMethodField()

    def get_researcher_level(self, researcher: models.Researcher):
        level = researcher.level
        if level == 'P':
            return 'Primary Author'
        return 'Secondary Author'

    def get_researcher_status(self, researcher: models.Researcher):
        status = researcher.status
        if status == 'A':
            return 'Active'
        return 'Inactive'


class ProjectEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SALOG_Employee
        fields = ['id', 'designation', 'rank', 'date_started', 'status']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ['id', 'title', 'SALOG_Employee', 'project_description',
                  'status', 'date_started', 'date_ended', 'duration']

    SALOG_Employee = serializers.SerializerMethodField()

    def get_SALOG_Employee(self, project: models.Project):
        employees = []
        queryset = project.project_employee.all()
        for project in queryset:
            employees.append(
                project.employee.id)
            # project.employee.person.get_full_name())
        return employees
