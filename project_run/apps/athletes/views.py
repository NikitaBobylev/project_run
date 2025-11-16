from django.http import HttpRequest
from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from project_run.apps.athletes.models import AthleteInfo
from project_run.apps.athletes.serializers import AthleteInfoSerializer


class AtheleteApiView(APIView):
    model: models.Model = AthleteInfo
    queryset = model.objects.all()
    serializer_class = AthleteInfoSerializer
    valid_statuses = {}

    def get_queryset(self):
        return self.queryset.select_related("user")

    def get(self, request: HttpRequest, user_id: int) -> Response:
        get_object_or_404(get_user_model(), pk=user_id)
        athelete, _ = self.model.objects.get_or_create(
            user_id=user_id,
        )
        serializer = self.serializer_class(athelete, many=False)
        return Response(serializer.data)

    def put(self, request: HttpRequest, user_id: int) -> Response:
        get_object_or_404(get_user_model(), pk=user_id)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        self.model.objects.update_or_create(
            user_id=user_id, defaults=serializer.validated_data
        )
        return Response(status=status.HTTP_201_CREATED)
