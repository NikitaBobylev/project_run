from django.urls import path

from project_run.apps.challenges.views import ChallengesApiView, ChallengeSummaru

urlpatterns = [
    path("challenges/", ChallengesApiView.as_view()),
    path("challenges_summary/", ChallengeSummaru.as_view({"get": "list"}, )),
]
