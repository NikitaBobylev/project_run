from django.urls import path, include

from rest_framework.routers import DefaultRouter

from project_run.apps.subscriptions.views import SubscriptionViewSet, RatingViewSet


urlpatterns = [
    path("subscribe_to_coach/<int:coach>/", SubscriptionViewSet.as_view({"post": "create"})),
    path("rate_coach/<int:coach>/", RatingViewSet.as_view())

]
