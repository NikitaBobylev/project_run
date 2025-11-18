from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, request, response, viewsets, mixins, status, exceptions


from project_run.apps.subscriptions.models import Subscriptions
from project_run.apps.subscriptions.serializers import CreateSubscriptionsSerializer


class SubscriptionViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet): 
    serializer_class = CreateSubscriptionsSerializer
    model = Subscriptions
    def create(self, request: request.Request, coach: int,  *args, **kwargs) -> response.Response:
        coach_obj = get_object_or_404(User, pk=coach)
        self.get_serializer(data=request.data).is_valid(raise_exception=True)
        self.validate_coach(coach_obj) 
        sub = Subscriptions(
            coach=coach_obj,
            athlete_id=request.data["athlete"]
        )
        sub.save()
        return response.Response(status=status.HTTP_200_OK)
    def get_queryset(self):
        return self.model.objects.all()
    
    def validate_coach(self, obj):
        if not obj.is_staff or obj.is_superuser:
            raise exceptions.ValidationError("User is not a coach")
        return obj