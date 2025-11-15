from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, SerializerMethodField, IntegerField


base_user_fields = ["id", "username", "last_name", "first_name"]

class GetRunsUserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields = base_user_fields.copy()

    
class GetUserSerializer(ModelSerializer):
    type = SerializerMethodField()
    runs_finished = IntegerField()

    def get_type(self, obj): 
        return obj.type

    def get_runs_finished(self, obj):
        return obj.runs_finished

    class Meta:
        model = User
        fields = base_user_fields + ["date_joined", "type", "runs_finished"]
