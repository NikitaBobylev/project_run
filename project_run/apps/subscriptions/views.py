from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import viewsets, request, response, views, mixins, status, exceptions


from project_run.apps.subscriptions.models import Subscriptions
from project_run.apps.subscriptions.serializers import CreateSubscriptionsSerializer, RatingSubscriptionsSerializer



def validate_coach(obj):
    if not obj.is_staff or obj.is_superuser:
        raise exceptions.ValidationError("User is not a coach")
    return obj


class SubscriptionViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet): 
    serializer_class = CreateSubscriptionsSerializer
    model = Subscriptions
    def create(self, request: request.Request, coach: int,  *args, **kwargs) -> response.Response:
        coach_obj = get_object_or_404(User, pk=coach)
        self.get_serializer(data=request.data).is_valid(raise_exception=True)
        validate_coach(coach_obj) 
        sub = Subscriptions(
            coach=coach_obj,
            athlete_id=request.data["athlete"]
        )
        sub.save()
        return response.Response(status=status.HTTP_200_OK)

    def get_queryset(self):
        return self.model.objects.all()


class RatingViewSet(views.APIView): 
    serializer_class = RatingSubscriptionsSerializer
    model = Subscriptions

    def post(self, request: request.Request, coach: int,  *args, **kwargs) -> response.Response:
        coach_obj = get_object_or_404(User, pk=coach)
        validate_coach(coach_obj) 
        self.serializer_class(data=request.data).is_valid(raise_exception=True)
        sub = self.get_queryset().filter(
            Q(coach=coach_obj) & 
            Q(athlete_id=request.data["athlete"])
        ).first()

        if sub is None:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

        sub.rating = request.data["rating"]
        sub.save()
        return response.Response(status=status.HTTP_200_OK)
    def get_queryset(self):
        return self.model.objects.all()