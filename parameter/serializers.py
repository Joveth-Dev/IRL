from rest_framework import serializers
from . import models


class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Research
        fields = ['researchers', 'title', 'description',
                  'status', 'date_started', 'date_ended', 'duration']

    researchers = serializers.SerializerMethodField()

    def get_researchers(self, research: models.Research):
        return str(research.researcher)
