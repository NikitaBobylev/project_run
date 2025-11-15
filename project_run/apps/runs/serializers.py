from rest_framework.serializers import ModelSerializer


from project_run.apps.runs.models import Runs
from project_run.apps.users.serializers import GetRunsUserSerializer


class RunsSerializer(ModelSerializer):
    athlete_data = GetRunsUserSerializer(source="athlete", read_only=True)
    class Meta:
        model = Runs
        fields = "__all__"
