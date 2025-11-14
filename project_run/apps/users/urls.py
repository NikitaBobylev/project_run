from django.urls import path, include

from rest_framework.routers import DefaultRouter

from project_run.apps.users.views import ReadOnlyUsersViewSet

router = DefaultRouter()

router.register("users", ReadOnlyUsersViewSet)

urlpatterns = [path("", include(router.urls))]
