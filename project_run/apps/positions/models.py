from django.db import models

from project_run.apps.common.models import CreatedAtTimeStampedModel
from project_run.apps.runs.models import Runs


class Positions(CreatedAtTimeStampedModel):
    run = models.ForeignKey(Runs, on_delete=models.CASCADE, related_name="positions")
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)
    