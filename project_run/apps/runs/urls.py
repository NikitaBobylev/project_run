from django.urls import path

from rest_framework.routers import DefaultRouter

from project_run.apps.runs.views import RunsViewSet

router = DefaultRouter()


urlpatterns = [
    path("runs/", RunsViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "runs/<int:pk>/",
        RunsViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
