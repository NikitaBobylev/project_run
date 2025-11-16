from django.urls import path, include

from rest_framework.routers import DefaultRouter

from project_run.apps.positions.views import PositionsViewSet

router = DefaultRouter()

router.register("positions", PositionsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
