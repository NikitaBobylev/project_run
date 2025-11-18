from rest_framework import serializers, exceptions


from project_run.apps.subscriptions.models import Subscriptions


class CreateSubscriptionsSerializer(serializers.ModelSerializer):
    def validate_athlete(self, obj):
        if obj.is_staff or obj.is_superuser:
            raise exceptions.ValidationError("User is not an athlete")
        return obj

    class Meta:
        model = Subscriptions
        fields = [
            "athlete",
        ]


class ValidateSubscriptionSerailzer(CreateSubscriptionsSerializer):

    def validate_coach(self, obj):
        if not obj.is_staff or obj.is_superuser:
            raise exceptions.ValidationError("User is not a coach")
        return obj

    class Meta:
        model = Subscriptions
        fields = "__all__"
