from enum import Enum

from django.db import models
from django.contrib.auth.models import User

from project_run.apps.common.models import CreatedAtTimeStampedModel


class RunsStatusEnums(str, Enum):
    _init: str = "init"
    in_progress: str = "in_progress"
    finished: str = "finished"


class Runs(CreatedAtTimeStampedModel):
    athlete = models.ForeignKey(User, on_delete=models.CASCADE, related_name="runs")
    comment = models.TextField()
    status = models.CharField(
        choices=[(status.value, status.value) for status in RunsStatusEnums],
        default=RunsStatusEnums._init.value,
    )
    distance = models.DecimalField(
        max_digits=9, decimal_places=4, null=True, blank=True, default=None
    )

    run_time_seconds = models.IntegerField(
        default=None, blank=True, null=True,
    )

    def save(self, commit=False, *args, **kwargs):
        return super().save(*args, **kwargs)
