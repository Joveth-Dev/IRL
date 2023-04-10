from rest_framework.viewsets import ReadOnlyModelViewSet
from . import models, serializers


class ActivityViewSet(ReadOnlyModelViewSet):
    queryset = models.Activity.objects. \
        select_related('project', 'research'). \
        filter(is_posted=True)
    serializer_class = serializers.ActivitySerializers


class NewsViewSet(ReadOnlyModelViewSet):
    queryset = models.News.objects. \
        select_related('project', 'research'). \
        filter(is_posted=True)
    serializer_class = serializers.NewsSerializers
