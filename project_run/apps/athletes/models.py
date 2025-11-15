from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_weight(value: int):
    
    if not 0 < value < 900:
        raise ValidationError(
            _("%(value)s is not an valid number"),
            params={"value": value},
        )

class AthleteInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.IntegerField(null=False, validators=[validate_weight], default=1)
    goals = models.FloatField(null=False, default=0)
