from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    Serializer,
    FileField,
    URLField,
)
from project_run.apps.positions.models import (
    validate_latitude as validate_latitude_db,
    validate_longitude as validate_longitude_db,
)

from project_run.apps.collectibleitems.models import CollectibleItems

base_fields = ["uid", "name", "value", "latitude", "longitude"]


class UploadCollectibleFileSerializer(Serializer):
    file = FileField()


class CollectibleItemsSerializerInput(ModelSerializer):
    uid = CharField()
    url = URLField(source="picture")

    def validate_latitude(self, value):
        validate_latitude_db(value=value)
        return value

    def validate_longitude(self, value):
        validate_longitude_db(value=value)
        return value

    class Meta:
        model = CollectibleItems
        fields = base_fields + ["url"]


class CollectibleItemsSerializerOutput(ModelSerializer):

    class Meta:
        model = CollectibleItems
        fields = base_fields + ["picture"]
