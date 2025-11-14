from rest_framework.serializers import ModelSerializer

from core.apps.runs.models import Runs


class RunsSerializer(ModelSerializer):
    class Meta: 
        model = Runs
        fields = '__all__'
