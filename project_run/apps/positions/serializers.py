from rest_framework.serializers import ModelSerializer, DecimalField
from rest_framework.exceptions import ValidationError


from project_run.apps.positions.models import (
    Positions,
    validate_latitude as validate_latitude_db,
    validate_longitude as validate_longitude_db,
)
from project_run.apps.runs.models import RunsStatusEnums


class PositionSerilizer(ModelSerializer):
    latitude = DecimalField(max_digits=7, decimal_places=4, required=True)
    longitude = DecimalField(max_digits=7, decimal_places=4, required=True)

    def validate_latitude(self, value):
        validate_latitude_db(value=value)
        return value

    def validate_longitude(self, value):
        validate_longitude_db(value=value)
        return value

    def validate_run(self, run):
        if run.status != RunsStatusEnums.in_progress.value:
            raise ValidationError(
                "Incorred status for create position need in_progress"
            )
        return run

    class Meta:
        model = Positions
        fields = ["longitude", "run", "latitude", "id"]
