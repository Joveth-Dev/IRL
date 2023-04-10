from rest_framework.viewsets import ReadOnlyModelViewSet
from . import models, serializers


class PersonViewSet(ReadOnlyModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class CoordinatorViewSet(ReadOnlyModelViewSet):
    queryset = models.Coordinator.objects.all()
    serializer_class = serializers.CoordinatorSerializer


class ProgramViewSet(ReadOnlyModelViewSet):
    queryset = models.Program.objects. \
        select_related('coordinator'). \
        filter(is_posted=True)
    serializer_class = serializers.ProgramSerializer


class SALOG_EmployeeViewSet(ReadOnlyModelViewSet):
    queryset = models.SALOG_Employee.objects. \
        select_related('person'). \
        all()
    serializer_class = serializers.SALOG_EmployeeSerializer


class ProjectViewSet(ReadOnlyModelViewSet):
    queryset = models.Project.objects. \
        prefetch_related('SALOG_employees__person'). \
        filter(is_posted=True)
    serializer_class = serializers.ProjectSerializer


class LinkagePartnerViewSet(ReadOnlyModelViewSet):
    queryset = models.LinkagePartner.objects.all()
    serializer_class = serializers.LinkagePartnerSerializer


class EquipmentViewSet(ReadOnlyModelViewSet):
    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSerializer


class ResearcherViewSet(ReadOnlyModelViewSet):
    queryset = models.Researcher.objects. \
        select_related('SALOG_employee__person'). \
        all()
    serializer_class = serializers.ResearcherSerializer


class ResearchViewSet(ReadOnlyModelViewSet):
    queryset = models.Research.objects. \
        select_related('project'). \
        prefetch_related('linkage_partners', 'researchers__SALOG_employee__person', 'equipments'). \
        filter(is_posted=True)
    serializer_class = serializers.ResearchSerializer
