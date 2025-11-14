from django.http import HttpRequest
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def company_view(request: HttpRequest):
    return Response(
        {
            "company_name": settings.COMPANY_NAME,
            "slogan": settings.COMPANY_DESCR,
            "contacts": settings.COMPANY_CONTACT,
        }
    )
