from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q, Max, Avg, Min, Sum
from rest_framework import (
    viewsets,
    request,
    response,
    views,
    mixins,
    status,
    exceptions,
)


from project_run.apps.subscriptions.models import Subscriptions
from project_run.apps.runs.models import Runs, RunsStatusEnums
from project_run.apps.subscriptions.serializers import (
    CreateSubscriptionsSerializer,
    RatingSubscriptionsSerializer,
    AnalitycsSerializer
)


def validate_coach(obj):
    if not obj.is_staff or obj.is_superuser:
        raise exceptions.ValidationError("User is not a coach")
    return obj


class SubscriptionViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CreateSubscriptionsSerializer
    model = Subscriptions

    def create(
        self, request: request.Request, coach: int, *args, **kwargs
    ) -> response.Response:
        coach_obj = get_object_or_404(User, pk=coach)
        self.get_serializer(data=request.data).is_valid(raise_exception=True)
        validate_coach(coach_obj)
        sub = Subscriptions(coach=coach_obj, athlete_id=request.data["athlete"])
        sub.save()
        return response.Response(status=status.HTTP_200_OK)

    def get_queryset(self):
        return self.model.objects.all()


class RatingViewSet(views.APIView):
    serializer_class = RatingSubscriptionsSerializer
    model = Subscriptions

    def post(
        self, request: request.Request, coach: int, *args, **kwargs
    ) -> response.Response:
        coach_obj = get_object_or_404(User, pk=coach)
        validate_coach(coach_obj)
        self.serializer_class(data=request.data).is_valid(raise_exception=True)
        sub = (
            self.get_queryset()
            .filter(Q(coach=coach_obj) & Q(athlete_id=request.data["athlete"]))
            .first()
        )

        if sub is None:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

        sub.rating = request.data["rating"]
        sub.save()
        return response.Response(status=status.HTTP_200_OK)

    def get_queryset(self):
        return self.model.objects.all()


class AnalitycsApiView(views.APIView):

    serializer_class = RatingSubscriptionsSerializer

    def get(
        self, request: request.Request, coach: int, *args, **kwargs
    ) -> response.Response:
        print("COACH REQUST --------------------")
        coach_obj = User.objects.prefetch_related("atheltes_sub").filter(id=coach).first()
        if coach_obj is None:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        validate_coach(coach_obj)
        print("-----------------------------")
        print()
        print("RUNS REQUSTS ------------------------------")
        runs = Runs.objects.select_related("athlete").filter(
            Q(status=RunsStatusEnums.finished.value) & 
            Q(athlete_id__in=coach_obj.atheltes_sub.all().values_list("athlete_id", flat=True))
        )
        print()
        res = {
            'longest_run_user': None,
            'longest_run_value': None, 
            'total_run_user': None, 
            'total_run_value': None,
            'speed_avg_user': None,
            'speed_avg_value': None
        }
        print("distance_req REQUST --------------")
        distance_req = runs.order_by("-distance").first()
        print()
        if distance_req:
            res["longest_run_user"] = distance_req.athlete_id
            res["longest_run_value"] = distance_req.distance

        print("run_user_req requst -----------")
        run_user_req = runs.values("athlete_id").annotate(
            total=Sum("distance"),
            avg_speed=Avg("speed")
        )
        print()

        print('total_run_user_req')
        total_run_user_req = run_user_req.order_by("-total").first()
        if total_run_user_req:
            res["total_run_user"] = total_run_user_req["athlete_id"]
            res["total_run_value"] = total_run_user_req["total"]
        print()
        print("avg_speed_run_user_req")
        avg_speed_run_user_req = run_user_req.order_by("-avg_speed").first() 

        if avg_speed_run_user_req:
            res["speed_avg_user"] = avg_speed_run_user_req["athlete_id"]
            res["speed_avg_value"] = avg_speed_run_user_req["avg_speed"]



        return response.Response(res)
