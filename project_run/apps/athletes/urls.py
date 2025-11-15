from django.urls import path

from project_run.apps.athletes.views import AtheleteApiView


urlpatterns = [
    # path("", include(router.urls)),
    path("athlete_info/<int:user_id>/", AtheleteApiView.as_view()),
    # path("runs/<int:pk>/stop/", StopRunApiView.as_view()),
]
