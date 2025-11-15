from rest_framework.filters import OrderingFilter
from django.contrib.auth.models import User
from django.db import models
from django.db.models import QuerySet, Q, Value, CharField, Case, When, Count, F, Prefetch

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter

from project_run.apps.runs.models import Runs, RunsStatusEnums
from project_run.apps.users.serializers import GetUserSerializer
from project_run.apps.common.filters import CommonAppPagination

class ReadOnlyUsersViewSet(ReadOnlyModelViewSet):
    _user_types = {"coach": True, "athlete": False}
    _user_types_reversd = {val: key for key, val in _user_types.items()}
    model: models.Model = User
    queryset = model.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["first_name", "last_name"]
    ordering_fields = ["date_joined"]
    serializer_class = GetUserSerializer
    pagination_class = CommonAppPagination

    def get_user_param_type(self) -> str | None:
        param_user_type = self.request.query_params.get("type", None)

        if self._user_types.get(param_user_type, None) is None:
            param_user_type = None

        return param_user_type

    def _build_query(self) -> Q:
        qs = Q(
            is_superuser=False,
        )
        param_exist = self.get_user_param_type()
        if param_exist is not None:
            qs &= Q(is_staff=self._user_types[param_exist])
        return qs

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset.prefetch_related(
            Prefetch("runs", Runs.objects.all().filter(
                status=RunsStatusEnums.finished.value
            ))
        ).filter(self._build_query()
            ).annotate(
                type=Case(
                    When(
                        is_staff=True,
                        then=Value(
                            self._user_types_reversd[True], output_field=CharField()
                        ),
                    ),
                    When(
                        is_staff=False,
                        then=Value(
                            self._user_types_reversd[False], output_field=CharField()
                        ),
                    ),
                )
            ).annotate(
                runs_finished=Count(F("runs"))
            )

        return queryset
