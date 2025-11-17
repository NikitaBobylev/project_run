from django_filters.rest_framework import DjangoFilterBackend
from django.db import models

from rest_framework import mixins, viewsets

from project_run.apps.positions.models import Positions
from project_run.apps.positions.serializers import PositionSerilizer


class PositionsViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    model: models.Model = Positions
    queryset = model.objects.select_related("run").all()
    serializer_class = PositionSerilizer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["run"]
