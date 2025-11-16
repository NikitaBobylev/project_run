from django.http import HttpRequest
from django.db import models
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from project_run.apps.challenges.models import Challenges
from project_run.apps.challenges.serializers import ChallengeSerializer, ChallengeParamSerializer


class ChallengesApiView(APIView):
    model: models.Model = Challenges
    queryset = model.objects.all().select_related("athlete")
    serializer_class = ChallengeSerializer
    param_serializer = ChallengeParamSerializer

    def __build_query(self, user_id):
        if user_id is not None:
            return Q(athlete_id=user_id)
        return Q()

    def get(self, request: HttpRequest, *args, **kwargs) -> Response:
        param_serializer = self.param_serializer(data=request.query_params) 
        param_serializer.is_valid(raise_exception=True)
        user_id = param_serializer.validated_data.get("athlete", None)
        challenges = self.queryset.filter(self.__build_query(user_id=user_id))

        return Response(
            data=self.serializer_class(challenges, many=True).data,
            status=status.HTTP_200_OK
        )
