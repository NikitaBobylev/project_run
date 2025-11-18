from django.urls import path, include

from rest_framework.routers import DefaultRouter

from project_run.apps.subscriptions.views import SubscriptionViewSet

# router = DefaultRouter()

# router.register("subscribe_to_coach/<int:id>/", RunsViewSet)

urlpatterns = [
    path("subscribe_to_coach/<int:coach>/", SubscriptionViewSet.as_view({"post": "create"}))

]
