from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    IntegerField,
)

from project_run.apps.challenges.models import Challenges


class ChallengeParamSerializer(Serializer):
    athlete = IntegerField(required=False)


class ChallengeSerializer(ModelSerializer):
    class Meta:
        model = Challenges
        fields = ["full_name", "athlete"]
