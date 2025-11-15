from django.contrib import admin

from project_run.apps.athletes.models import AthleteInfo
# Register your models here.

@admin.register(AthleteInfo)
class AthleteInfo(admin.ModelAdmin): 
    ...
