from rest_framework import serializers
from . import models


class ActivitySerializers(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    research = serializers.StringRelatedField()

    class Meta:
        model = models.Activity
        fields = ['id', 'project', 'research', 'name', 'description', 'activity_type',
                  'date_started', 'date_ended', 'duration_in_hours', 'date_posted']


class NewsSerializers(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    research = serializers.StringRelatedField()

    class Meta:
        model = models.News
        fields = ['id', 'project', 'research', 'name', 'details',
                  'category', 'date_posted', 'date_expired', 'status']
