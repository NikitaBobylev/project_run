from decimal import Decimal
from django.db.models import Q
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from geopy.distance import geodesic

from project_run.apps.positions.models import Positions
from project_run.apps.collectibleitems.models import (
    CollectibleItems,
    UsersCollectionsItems,
)


@receiver(post_save, sender=Positions)
def check_collectible_items(
    sender: type[Positions], instance: Positions, created, **kwargs
):
    curent_items: CollectibleItems = CollectibleItems.objects.all()
    res_collections = []

    for item in curent_items:
        current_distance = geodesic(
            (instance.latitude, instance.longitude),
            (item.latitude, item.longitude),
        ).meters

        if current_distance <= 100:
            res_collections.append(item.id)

    existinng_items = UsersCollectionsItems.objects.filter(
        Q(user_id=instance.run.athlete_id) & Q(collection_id__in=res_collections)
    ).values_list("collection_id", flat=True)

    existinng_items = set(existinng_items)

    items_users_to_save = [
        UsersCollectionsItems(user_id=instance.run.athlete_id, collection_id=item_id)
        for item_id in res_collections
        if item_id not in existinng_items
    ]
    UsersCollectionsItems.objects.bulk_create(items_users_to_save)


@receiver(pre_save, sender=Positions)
def calculate_position(sender: type[Positions], instance: Positions, **kwargs):
    all_positions = sender.objects.filter(
        Q(run_id=instance.run_id) & ~Q(id=instance.id)
    ).order_by("created_at")

    prev_position = all_positions.last()

    if prev_position:
        disntace_geo_last = geodesic(
            (prev_position.latitude, prev_position.longitude),
            (instance.latitude, instance.longitude),
        )
        full_run_disntace: Decimal = Decimal(disntace_geo_last.kilometers)

        for position in all_positions:
            full_run_disntace += Decimal(position.distance)

        instance.distance = float(round(full_run_disntace, 2))
        time_spend_seconds = (instance.created_at - prev_position.created_at).seconds
        instance.speed = float(round(disntace_geo_last.meters / time_spend_seconds, 2))
