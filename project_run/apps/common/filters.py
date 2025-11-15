from rest_framework.pagination import PageNumberPagination


class CommonAppPagination(PageNumberPagination):
    page_size_query_param = (
        "size"
    )