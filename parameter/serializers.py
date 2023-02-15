from rest_framework import serializers
from . import models


class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Research
        fields = ['id', 'title', 'description', 'author', 'status',
                  'date_started', 'date_ended', 'duration']

    author = serializers.SerializerMethodField()

    def get_author(self, research: models.Research):
        researchers = []
        queryset = research.researcher.all()
        for researcher in queryset:
            researchers.append(
                researcher.SALOG_employee.person.get_full_name())
        return researchers


# ============= This classes will be displayed in the researchers/ endpoint =============
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'extension_name',
                  'permanent_address', 'current_address', 'municipality', 'email']


class SALOG_EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SALOG_Employee
        fields = ['id', 'person', 'designation',
                  'rank', 'date_started', 'status']

    person = PersonSerializer()
# =======================================================================================


class ResearcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Researcher
        fields = ['id', 'SALOG_employee',
                  'researcher_level', 'researcher_status']

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


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ['id', 'title', 'description', 'status',
                  'date_started', 'date_ended', 'duration']
