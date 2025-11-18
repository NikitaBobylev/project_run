from django.db import models

from django.contrib.auth.models import User


class Subscriptions(models.Model):
    athlete = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name="coach_sub")
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name="atheltes_sub")
