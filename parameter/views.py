from rest_framework.viewsets import ReadOnlyModelViewSet
from . import serializers
from . import models


class PersonViewSet(ReadOnlyModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class ResearchViewSet(ReadOnlyModelViewSet):
    queryset = models.Research.objects.all()
    serializer_class = serializers.ResearchSerializer


class ResearcherViewSet(ReadOnlyModelViewSet):
    queryset = models.Researcher.objects.all()
    serializer_class = serializers.ResearcherSerializer


class ProjectViewSet(ReadOnlyModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class SALOG_EmployeeViewSet(ReadOnlyModelViewSet):
    queryset = models.SALOG_Employee.objects.all()
    serializer_class = serializers.SALOG_EmployeeSerializer
