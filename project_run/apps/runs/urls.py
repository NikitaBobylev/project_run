from django.urls import path, include

from rest_framework.routers import DefaultRouter

from project_run.apps.runs.views import RunsViewSet, StartRunApiView, StopRunApiView

router = DefaultRouter()

router.register("runs", RunsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("runs/<int:pk>/start/", StartRunApiView.as_view()),
    path("runs/<int:pk>/stop/", StopRunApiView.as_view()),
]
