from django.contrib.auth.models import User
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    IntegerField,
)

from project_run.apps.collectibleitems.serializers import (
    CollectibleItemsSerializerOutput,
)

from project_run.apps.collectibleitems.models import CollectibleItems
from project_run.apps.subscriptions.models import Subscriptions

base_user_fields = [
    "id",
    "username",
    "last_name",
    "first_name",
]

get_user_fieds = ["date_joined", "type", "runs_finished", "rating"]


class GetRunsUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = base_user_fields.copy()


class ShortUserSerailizer(ModelSerializer):
    type = SerializerMethodField()
    runs_finished = IntegerField()
    rating = SerializerMethodField()

    def get_rating(self, obj):
        return obj.rating

    def get_type(self, obj):
        return obj.type

    def get_runs_finished(self, obj):
        return obj.runs_finished

    class Meta:
        model = User
        fields = base_user_fields + get_user_fieds


class UserDetailSerializser(ShortUserSerailizer):
    items = SerializerMethodField(read_only=True)
    coach_athlete = SerializerMethodField(read_only=True)

    def get_items(self, obj):
        items = CollectibleItems.objects.prefetch_related("users").filter(
            users__user_id=obj.id
        )
        return CollectibleItemsSerializerOutput(items, many=True).data

    def get_coach_athlete(self, obj):
        if obj.type == "coach":
            return Subscriptions.objects.filter(coach_id=obj.id).values_list(
                "athlete_id", flat=True
            )
        coach = Subscriptions.objects.filter(athlete_id=obj.id).first()
        if coach is None:
            return None
        return coach.coach_id

    def to_representation(self, instance):
        revers_dict = {"athlete": "coach", "coach": "athletes"}
        data = super().to_representation(instance).copy()
        data[revers_dict[instance.type]] = data.pop("coach_athlete")
        return data

    class Meta:
        model = User
        fields = base_user_fields + get_user_fieds + ["items", "coach_athlete"]



