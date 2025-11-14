from rest_framework.serializers import ModelSerializer

from project_run.apps.runs.models import Runs


class RunsSerializer(ModelSerializer):
    class Meta: 
        model = Runs
        fields = '__all__'
