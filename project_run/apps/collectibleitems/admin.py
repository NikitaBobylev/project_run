from django.contrib import admin

from project_run.apps.collectibleitems.models import CollectibleItems
# Register your models here.

@admin.register(CollectibleItems)
class CategoryAdmin(admin.ModelAdmin): 
    ...