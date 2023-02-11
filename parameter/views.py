from rest_framework.viewsets import ReadOnlyModelViewSet
from . import serializers
from . import models


class ResearchViewSet(ReadOnlyModelViewSet):
    queryset = models.Research.objects.select_related('researcher').all()
    serializer_class = serializers.ResearchSerializer
