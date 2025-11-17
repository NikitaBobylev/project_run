from django.db import models

from project_run.apps.positions.models import PositionsAbstract


class CollectibleItems(PositionsAbstract):
    name = models.CharField(max_length=100, null=False, blank=False)
    uid = models.CharField(max_length=100, null=False, blank=False)
    picture = models.URLField(null=False, blank=False)
    value = models.IntegerField(null=False, blank=False)
