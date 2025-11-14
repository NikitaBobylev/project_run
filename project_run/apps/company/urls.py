from django.urls import path

from rest_framework.routers import DefaultRouter

from project_run.apps.company.views import company_view

router = DefaultRouter()

urlpatterns = [
    path("company_details/", company_view),
]

