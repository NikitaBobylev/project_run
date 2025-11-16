from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.http import HttpRequest
from django.db import models
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from project_run.apps.runs.models import Runs as RunsModel, RunsStatusEnums
from project_run.apps.runs.serializers import RunsSerializer
from project_run.apps.common.filters import CommonAppPagination


def get_base_quesry_set(queryset: models.QuerySet):
    return queryset.select_related("athlete").prefetch_related("positions")


class RunsViewSet(ModelViewSet):
    model: models.Model = RunsModel
    queryset = model.objects.all()
    serializer_class = RunsSerializer
    valid_statuses = {}
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["status", "athlete"]
    ordering_fields = ["created_at"]
    pagination_class = CommonAppPagination

    def get_queryset(self):
        return get_base_quesry_set(self.queryset)


class BaseRunsApiView(APIView):
    model: models.Model = RunsModel
    queryset = model.objects.all()
    serializer_class = RunsSerializer
    valid_statuses = {}

    @property
    def action() -> models.Model:
        return RunsStatusEnums._init

    def get_queryset(self):
        return get_base_quesry_set(self.queryset)


    def post(self, request: HttpRequest, *args, **kwargs) -> Response:
        pk = kwargs.get("pk", None)
        if pk is None:
            curr_status = status.HTTP_404_NOT_FOUND
            return Response(data={}, status=curr_status)
        try:
            obj = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            curr_status = status.HTTP_404_NOT_FOUND
            return Response(data={}, status=curr_status)

        if obj.status not in self.valid_statuses:
            curr_status = status.HTTP_400_BAD_REQUEST
            return Response(data={}, status=curr_status)

        obj.status = self.action
        obj.save()
        curr_status = status.HTTP_200_OK
        return Response(data={}, status=curr_status)


class StartRunApiView(BaseRunsApiView):
    action = RunsStatusEnums.in_progress.value
    valid_statuses = {
        RunsStatusEnums._init.value,
    }


class StopRunApiView(BaseRunsApiView):
    action = RunsStatusEnums.finished.value
    valid_statuses = {
        RunsStatusEnums.in_progress.value,
    }
