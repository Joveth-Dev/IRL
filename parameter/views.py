from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet
from . import models, serializers


class PersonViewSet(ReadOnlyModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class CoordinatorViewSet(ReadOnlyModelViewSet):
    queryset = models.Coordinator.objects.all()
    serializer_class = serializers.CoordinatorSerializer


class ProgramViewSet(ReadOnlyModelViewSet):
    filter_backends = [SearchFilter]
    queryset = models.Program.objects. \
        select_related('coordinator'). \
        filter(is_posted=True)
    search_fields = ['title', 'executive_summary', 'coordinator__name']
    serializer_class = serializers.ProgramSerializer


class IRL_EmployeeViewSet(ReadOnlyModelViewSet):
    queryset = models.IRL_Employee.objects. \
        select_related('person'). \
        all()
    serializer_class = serializers.IRL_EmployeeSerializer


class ProjectViewSet(ReadOnlyModelViewSet):
    filter_backends = [SearchFilter]
    queryset = models.Project.objects. \
        select_related('program'). \
        prefetch_related('IRL_employees__person', 'agency_set'). \
        filter(is_posted=True)
    search_fields = [
        'program__title',
        'title',
        'project_description',
        'IRL_employees__person__first_name',
        'IRL_employees__person__middle_name',
        'IRL_employees__person__last_name',
    ]
    serializer_class = serializers.ProjectSerializer


class LinkagePartnerViewSet(ReadOnlyModelViewSet):
    queryset = models.LinkagePartner.objects.all()
    serializer_class = serializers.LinkagePartnerSerializer


class EquipmentViewSet(ReadOnlyModelViewSet):
    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSerializer


class ResearcherViewSet(ReadOnlyModelViewSet):
    queryset = models.Researcher.objects. \
        select_related('IRL_employee__person'). \
        all()
    serializer_class = serializers.ResearcherSerializer


class ResearchViewSet(ReadOnlyModelViewSet):
    filter_backends = [SearchFilter]
    queryset = models.Research.objects. \
        select_related('project'). \
        prefetch_related('linkage_partners', 'researchers__IRL_employee__person', 'equipment'). \
        filter(is_posted=True)
    search_fields = [
        'project__title',
        'title',
        'description',
        'researchers__IRL_employee__person__first_name',
        'researchers__IRL_employee__person__middle_name',
        'researchers__IRL_employee__person__last_name',
        'equipment__name',
        'equipment__description',
        'linkage_partners__name',
        'linkage_partners__description',
    ]
    serializer_class = serializers.ResearchSerializer
