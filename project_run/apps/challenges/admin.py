from django.contrib import admin

from project_run.apps.challenges.models import Challenges
# Register your models here.

@admin.register(Challenges)
class ChallengeAdmin(admin.ModelAdmin): 
    ...