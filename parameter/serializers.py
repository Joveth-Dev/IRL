from rest_framework import serializers
from . import models


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'extension_name',
                  'permanent_address', 'current_address', 'municipality', 'email']


class CoordinatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coordinator
        fields = ['id', 'name', 'sex', 'agency_or_address']


class ProgramSerializer(serializers.ModelSerializer):
    coordinator = CoordinatorSerializer()

    class Meta:
        model = models.Program
        fields = ['id', 'title', 'executive_summary',
                  'date_posted', 'coordinator']


class CustomPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ['id', 'first_name', 'middle_name',
                  'last_name', 'extension_name']


class IRL_EmployeeSerializer(serializers.ModelSerializer):
    person = CustomPersonSerializer()

    class Meta:
        model = models.IRL_Employee
        fields = ['id', 'designation', 'rank',
                  'date_started', 'status', 'person']


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agency
        fields = ['id', 'type', 'name', 'logo']


class ProjectSerializer(serializers.ModelSerializer):
    program = serializers.StringRelatedField()
    IRL_employees = IRL_EmployeeSerializer(many=True)
    agencies = AgencySerializer(
        source='agency_set',
        many=True,
    )

    class Meta:
        model = models.Project
        fields = ['id', 'program', 'title', 'project_summary', 'sampling_site', 'sampling_site_image',
                  'references', 'status', 'date_started', 'date_ended', 'duration', 'date_posted', 'IRL_employees', 'agencies']


class LinkagePartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LinkagePartner
        fields = ['id', 'name', 'description',
                  'logo', 'date_of_linkage', 'status']


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipment
        fields = ['id', 'name', 'description', 'image']


class ResearcherSerializer(serializers.ModelSerializer):
    IRL_employee = IRL_EmployeeSerializer()

    class Meta:
        model = models.Researcher
        fields = ['id', 'level', 'status', 'IRL_employee']


class ResearchSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    researchers = ResearcherSerializer(many=True)
    equipment = EquipmentSerializer(many=True)
    linkage_partners = LinkagePartnerSerializer(many=True)

    class Meta:
        model = models.Research
        fields = ['id', 'project', 'title', 'description', 'status', 'date_started', 'date_ended',
                  'duration', 'date_posted', 'researchers', 'equipment', 'linkage_partners']
