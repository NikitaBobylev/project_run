from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class GetUserSerializer(ModelSerializer):
    type = SerializerMethodField()


    def get_type(self, obj): 
        return obj.type

    class Meta:
        model = User
        fields = ["id", "date_joined", "username", "last_name", "first_name", "type"]
