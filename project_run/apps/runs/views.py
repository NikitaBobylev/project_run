from django.db import models
from rest_framework.viewsets import ModelViewSet

from project_run.apps.runs.models import Runs as RunsModel
from project_run.apps.runs.serializers import RunsSerializer


class RunsViewSet(ModelViewSet):
    model: models.Model = RunsModel
    queryset = model.objects.all()
    serializer_class = RunsSerializer