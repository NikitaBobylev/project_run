from django.db import models

from django.contrib.auth.models import User

from django.core.exceptions import ValidationError


def min_rating_validator(val):
    if val < 1:
        raise ValidationError("Incorrect value for rating")


def max_rating_validator(val):
    if val > 5:
        raise ValidationError("Incorrect value for rating")


class Subscriptions(models.Model):
    athlete = models.OneToOneField(
        User, unique=True, on_delete=models.CASCADE, related_name="coach_sub"
    )
    coach = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="atheltes_sub"
    )
    rating = models.IntegerField(
        null=True,
        default=None,
        blank=True,
        validators=[min_rating_validator, max_rating_validator],
    )
