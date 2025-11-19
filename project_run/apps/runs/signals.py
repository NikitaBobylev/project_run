from decimal import Decimal

from django.conf import settings
from django.db.models import Q, QuerySet, Sum, Avg
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


from project_run.apps.runs.models import Runs, RunsStatusEnums
from project_run.apps.challenges.models import Challenges


@receiver(post_save, sender=Runs)
def create_challege(sender, instance, created, **kwargs):
    if not created and instance.status == RunsStatusEnums.finished.value:
        athelte_runs_query_set: QuerySet = sender.objects.filter(
            Q(athlete_id=instance.athlete_id) & Q(status=RunsStatusEnums.finished.value)
        )
        if athelte_runs_query_set.count() == settings.CREATE_SIGNAL_CHALLENGE_COUNT:

            challenge = Challenges(
                full_name=f"Сделай {settings.CREATE_SIGNAL_CHALLENGE_COUNT} Забегов!",
                athlete=instance.athlete,
            )
            challenge.save()

        all_disntace = athelte_runs_query_set.aggregate(Sum("distance"))[
            "distance__sum"
        ]
        if all_disntace >= settings.CREATE_SIGNAL_CHALLENGE_50_COUNT:
            challenge = Challenges(
                full_name=f"Пробеги {settings.CREATE_SIGNAL_CHALLENGE_50_COUNT} километров!",
                athlete=instance.athlete,
            )
            challenge.save()

        if instance.distance >= 2 and instance.run_time_seconds / 60 <= 10:
            challenge = Challenges(
                full_name=f"2 километра за 10 минут!",
                athlete=instance.athlete,
            )
            challenge.save()


def __calculate_distance(instance: Runs, positions) -> Decimal:
    res = Decimal(0)
    pos = positions.last()
    if pos:
        res += Decimal(positions.last()["distance"])
    return res


def __calculate_run_time_seconds(positions):
    res = 0
    if len(positions) > 0:
        res = (positions.last()["created_at"] - positions.first()["created_at"]).seconds

    return res


@receiver(pre_save, sender=Runs)
def calculate_distance(sender, instance, *args, **kwargs):
    if instance.status == RunsStatusEnums.finished.value:
        positions: QuerySet = instance.positions.order_by("created_at").values()

        instance.distance = __calculate_distance(instance, positions)

        instance.run_time_seconds = __calculate_run_time_seconds(positions=positions)
        speed = 0
        positions_speed = positions.aggregate(Avg("speed"))["speed__avg"]

        if positions_speed is not None:
            speed += positions_speed

        instance.speed = float(
            round(speed, 2)
        )
