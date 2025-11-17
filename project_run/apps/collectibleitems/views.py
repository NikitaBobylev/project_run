from django.shortcuts import render

from django.http.request import HttpRequest
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

import openpyxl


from project_run.apps.collectibleitems.models import CollectibleItems
from project_run.apps.collectibleitems.serializers import (
    CollectibleItemsSerializer,
    UploadCollectibleFileSerializer,
)


class FileUploadView(views.APIView):
    # parser_classes = (FormParser, MultiPartParser, FileUploadParser)
    model = CollectibleItems
    serializer_class = UploadCollectibleFileSerializer
    items_serializer = CollectibleItemsSerializer

    def post(self, request: HttpRequest, format=None):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        wb = openpyxl.open(serializer.validated_data["file"])

        sheet_obj = wb.active

        first_row = [
            cell.value.lower() for cell in sheet_obj[1] if cell.value is not None
        ]

        validated_rows = []
        invalid_rows = []

        for row_i in range(2, sheet_obj.max_row + 1):
            row = sheet_obj[row_i]
            res_dict = {}
            list_for_ivalid_rows = []
            for header, cell in zip(first_row, row):
                res_dict[header] = cell.value
                list_for_ivalid_rows.append(cell.value)

            items_serializer = self.items_serializer(data=res_dict)
            if not items_serializer.is_valid():
                invalid_rows.append(list_for_ivalid_rows)
                continue

            if res_dict:
                validated_rows.append(items_serializer.validated_data)

        self.model.objects.bulk_create(
            [self.model(**vlaidated_row) for vlaidated_row in validated_rows]
        )

        return Response(status=200, data=invalid_rows)


class CollectibleItemeViewSet(ListModelMixin, GenericViewSet):
    model = CollectibleItems
    serializer_class = CollectibleItemsSerializer
    queryset = model.objects.all()
