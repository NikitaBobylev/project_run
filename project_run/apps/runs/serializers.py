from rest_framework.serializers import ModelSerializer, IntegerField


from project_run.apps.runs.models import Runs
from project_run.apps.users.serializers import GetRunsUserSerializer


class RunsSerializer(ModelSerializer):
    athlete_data = GetRunsUserSerializer(source="athlete", read_only=True)
    run_time_seconds = IntegerField(read_only=True)
    distance = IntegerField(read_only=True)
    class Meta:
        model = Runs
        fields = "__all__"
