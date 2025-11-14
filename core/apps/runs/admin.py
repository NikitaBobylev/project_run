from django.contrib import admin

from core.apps.runs.models import Runs
# Register your models here.

@admin.register(Runs)
class CategoryAdmin(admin.ModelAdmin): 
    ...