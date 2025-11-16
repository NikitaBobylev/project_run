from decimal import Decimal

from django.conf import settings
from django.db.models import Q
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from geopy.distance import geodesic


from project_run.apps.runs.models import Runs, RunsStatusEnums
from project_run.apps.challenges.models import Challenges


@receiver(post_save, sender=Runs)
def create_challege(sender, instance, created, **kwargs):
    if (
        not created
        and instance.status == RunsStatusEnums.finished.value
        and sender.objects.filter(
            Q(athlete_id=instance.athlete_id) & Q(status=RunsStatusEnums.finished.value)
        ).count()== settings.CREATE_SIGNAL_CHALLENGE_COUNT
    ):
        challenge = Challenges(full_name="Сделай 10 Забегов!", athlete=instance.athlete)
        challenge.save()



def __calculate_distance(instance: Runs) -> Decimal:
        res = Decimal(0)
        positions = instance.positions.order_by("created_at").values()

        for position in range(1, len(positions)):
            first = positions[position - 1]
            last = positions[position]
            res += Decimal(
                geodesic(
                    (first["latitude"], last["latitude"]),
                    (last["latitude"], last["latitude"]),
                ).kilometers
            )

        return res


@receiver(pre_save, sender=Runs)
def calculate_distance(**kwargs):
    if kwargs["instance"].status == RunsStatusEnums.finished.value:
        kwargs["instance"].distance = __calculate_distance(kwargs["instance"])