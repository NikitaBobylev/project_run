from django.http import HttpRequest
from django.db import models
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets


from project_run.apps.challenges.models import Challenges
from project_run.apps.challenges.serializers import (
    ChallengeSerializer,
    ChallengeParamSerializer,
)


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
            status=status.HTTP_200_OK,
        )


class ChallengeSummaru(mixins.ListModelMixin, viewsets.GenericViewSet):
    model = Challenges

    def get_challenges_summary(self):
        challenges_data = Challenges.objects.select_related("athlete").values(
            "full_name",
            "athlete__id",
            "athlete__first_name",
            "athlete__last_name",
            "athlete__username",
        )
        challenges_users = {} 
        resulst = {}
        

        for challenge in challenges_data:
            name_to_display = challenge["full_name"]


            if name_to_display not in resulst:
                resulst[name_to_display] = {"name_to_display": name_to_display, "athletes": []}
                challenges_users[name_to_display] = set()


            user_id = challenge["athlete__id"]
            if user_id not in challenges_users[name_to_display]:
                challenges_users[name_to_display].add(user_id) 
                resulst[name_to_display]["athletes"].append(
                    {
                        "id": user_id,
                        "full_name": challenge["athlete__first_name"] + " " + challenge["athlete__last_name"],
                        "username": challenge["athlete__username"]
                    }
                )
        return resulst.values()


    def list(self, request, *args, **kwargs):
        data = self.get_challenges_summary()
        return Response(data)
