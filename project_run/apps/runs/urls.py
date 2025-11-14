from django.urls import path

from rest_framework.routers import DefaultRouter

from project_run.apps.runs.views import RunsViewSet

router = DefaultRouter()


urlpatterns = [
    path("runs/", RunsViewSet.as_view({'get': 'list'})),
]
