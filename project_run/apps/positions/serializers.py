from rest_framework.serializers import ModelSerializer, DecimalField
from rest_framework.exceptions import ValidationError


from project_run.apps.positions.models import Positions


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

    
    class Meta:
        model = Positions
        fields = ["longitude", "run", "latitude", "id"]

