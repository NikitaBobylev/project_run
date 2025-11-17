from django.db import models
from django.contrib.auth.models import User

from project_run.apps.positions.models import PositionsAbstract


class CollectibleItems(PositionsAbstract):
    name = models.CharField(max_length=100, null=False, blank=False)
    uid = models.CharField(max_length=100, null=False, blank=False)
    picture = models.URLField(null=False, blank=False)
    value = models.IntegerField(null=False, blank=False)


class UsersCollectionsItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collections")
    collection = models.ForeignKey(
        CollectibleItems, on_delete=models.CASCADE, related_name="users"
    )

    class Meta:
        db_table = "users_items"
        unique_together = ["user", "collection"]
