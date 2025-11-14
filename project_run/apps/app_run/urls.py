from django.urls import path, include

from rest_framework.routers import DefaultRouter

from project_run.apps.app_run.views import company_view

router = DefaultRouter()

urlpatterns = [
    # path("hello-world/", hello_world_post),
    path("company_details/", company_view),
]

