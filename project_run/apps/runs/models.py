from django.db import models
from django.contrib.auth.models import User

from project_run.apps.common.models import CreatedAtTimeStampedModel
# Create your models here.

class Runs(CreatedAtTimeStampedModel): 
    athlete = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="runs"
    )
    comment = models.TextField()