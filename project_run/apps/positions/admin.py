from django.contrib import admin

from project_run.apps.positions.models import Positions
# Register your models here.

@admin.register(Positions)
class CategoryAdmin(admin.ModelAdmin): 
    ...