from django.db import models
from django.db.models import F
from rest_framework.viewsets import ModelViewSet

from project_run.apps.runs.models import Runs as RunsModel
from project_run.apps.runs.serializers import RunsSerializer


class RunsViewSet(ModelViewSet):
    model: models.Model = RunsModel
    queryset = model.objects.all()
    serializer_class = RunsSerializer

    def get_queryset(self):
        return self.queryset.select_related("athlete").annotate()
