from django.urls import path

from project_run.apps.challenges.views import ChallengesApiView  

urlpatterns = [
    path("challenges/", ChallengesApiView.as_view()),
]
