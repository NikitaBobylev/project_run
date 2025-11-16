from rest_framework.serializers import ModelSerializer, IntegerField, CharField

from project_run.apps.athletes.models import AthleteInfo, validate_weight


class AthleteInfoSerializer(ModelSerializer):
    user_id = IntegerField(read_only=True)
    goals = CharField(required=False)
    weight = IntegerField(required=False)

    class Meta:
        model = AthleteInfo
        fields = ["weight", "goals", "user_id"]


    def validate_weight(self, value: int):
        validate_weight(value=value)
        return value