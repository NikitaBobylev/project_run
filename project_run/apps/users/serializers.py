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

base_user_fields = [
    "id",
    "username",
    "last_name",
    "first_name",
]

get_user_fieds = ["date_joined", "type", "runs_finished" ]


class GetRunsUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = base_user_fields.copy()

class GetUserSerializer(ModelSerializer):
    type = SerializerMethodField()
    runs_finished = IntegerField()

    def get_type(self, obj):
        return obj.type

    def get_runs_finished(self, obj):
        return obj.runs_finished

    class Meta:
        model = User
        fields = base_user_fields + get_user_fieds

class GetUserItemsSerializer(GetUserSerializer):
    items = SerializerMethodField(read_only=True)

    def get_items(self, obj):
        items = CollectibleItems.objects.prefetch_related("users").filter(
            users__user_id=obj.id
        )
        return CollectibleItemsSerializerOutput(items, many=True).data

    class Meta:
        model = User
        fields = base_user_fields + get_user_fieds + ["items"]
