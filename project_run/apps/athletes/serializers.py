from rest_framework.serializers import ModelSerializer, IntegerField

from project_run.apps.athletes.models import AthleteInfo, validate_weight


class AthleteInfoSerializer(ModelSerializer):
    user_id = IntegerField(read_only=True)
    goals = IntegerField(required=False, default=0)
    weight = IntegerField(validators=[validate_weight], default=1)


    class Meta:
        model = AthleteInfo
        fields = ["weight", "goals", "user_id"]