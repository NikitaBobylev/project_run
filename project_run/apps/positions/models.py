from django.db import models

from project_run.apps.common.models import CreatedAtTimeStampedModel
from project_run.apps.runs.models import Runs

from django.core.exceptions import ValidationError


def validate_latitude(value):
    if not -90.0 <= value <= 90:
        raise ValidationError("Incorrect latitude")
    return value


def validate_longitude(value):
    if not -180.0 <= value <= 180.0:
        raise ValidationError("Incorrect longitude")
    return value


class PositionsAbstract(CreatedAtTimeStampedModel):
    latitude = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[
            validate_latitude,
        ],
    )
    longitude = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[
            validate_longitude,
        ],
    )

    class Meta:
        abstract = True


class Positions(PositionsAbstract):
    run = models.ForeignKey(Runs, on_delete=models.CASCADE, related_name="positions")
