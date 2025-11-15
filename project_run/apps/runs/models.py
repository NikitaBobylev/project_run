from enum import Enum

from django.db import models
from django.contrib.auth.models import User

from project_run.apps.common.models import CreatedAtTimeStampedModel
# Create your models here.

class RunsStatusEnums(str, Enum): 
    _init: str = "init"
    in_progress :str = "in_progress"
    finished: str = "finished"

class Runs(CreatedAtTimeStampedModel): 
    athlete = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="runs"
    )
    comment = models.TextField()
    status = models.CharField(
        choices=[
            (status.value, status.value)
            for status in RunsStatusEnums
        ],
        default=RunsStatusEnums._init.value
    )