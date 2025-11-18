from rest_framework import viewsets, request, response, viewsets, mixins, status


from project_run.apps.subscriptions.models import Subscriptions
from project_run.apps.subscriptions.serializers import CreateSubscriptionsSerializer, ValidateSubscriptionSerailzer


class SubscriptionViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet): 
    serializer_class = CreateSubscriptionsSerializer
    model = Subscriptions
    def create(self, request: request.Request, coach: int,  *args, **kwargs) -> response.Response:
        data = request.data.dict().copy()
        
        data.update({
            "coach": coach
        })
        serializer = ValidateSubscriptionSerailzer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return response.Response(status=status.HTTP_200_OK)
    def get_queryset(self):
        return self.model.objects.all()
    
