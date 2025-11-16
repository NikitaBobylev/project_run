from rest_framework.serializers import ModelSerializer, DecimalField
from rest_framework.exceptions import ValidationError


from project_run.apps.positions.models import Positions
from project_run.apps.runs.models import RunsStatusEnums


class PositionSerilizer(ModelSerializer):
    latitude = DecimalField(max_digits=7, decimal_places=4, required=True)
    longitude = DecimalField(max_digits=7, decimal_places=4, required=True)


    def validate_latitude(self, value):
        if not -90.0 <= value <= 90: 
            raise ValidationError("Incorrect latitude")
        return value


    def validate_longitude(self, value):
        if not -180.0 <= value <= 180.0:
            raise ValidationError("Incorrect longitude")
        return value


    def validate_run(self, run):
        if run.status != RunsStatusEnums.in_progress.value:
            raise ValidationError("Incorred status for create position need in_progress")
        return run
    
    class Meta:
        model = Positions
        fields = ["longitude", "run", "latitude", "id"]

