from django.contrib import admin

from project_run.apps.subscriptions.models import Subscriptions
# Register your models here.

@admin.register(Subscriptions)
class SubsctiptionAdminModel(admin.ModelAdmin): 
    ...