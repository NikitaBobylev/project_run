from rest_framework import serializers, exceptions


from project_run.apps.subscriptions.models import Subscriptions, max_rating_validator, min_rating_validator


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


class RatingSubscriptionsSerializer(serializers.Serializer):
    rating = serializers.IntegerField(required=True)

    def validate_rating(self, val):
        max_rating_validator(val)
        min_rating_validator(val)
        return val

