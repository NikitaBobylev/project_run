from django.urls import path, include

from rest_framework.routers import DefaultRouter

from project_run.apps.runs.views import RunsViewSet

router = DefaultRouter()

router.register("runs", RunsViewSet)

urlpatterns = [path("", include(router.urls))]
