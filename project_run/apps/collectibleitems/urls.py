from django.urls import path, include

from rest_framework.routers import DefaultRouter

from project_run.apps.collectibleitems.views import FileUploadView, CollectibleItemeViewSet

router = DefaultRouter()

router.register("collectible_item", CollectibleItemeViewSet, basename="collectible_items")

urlpatterns = [
    path("", include(router.urls)),
    path("upload_file/", FileUploadView.as_view()),
]
