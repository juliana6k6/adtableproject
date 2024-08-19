from rest_framework.pagination import PageNumberPagination


class AdPaginator(PageNumberPagination):
    page_size = 4
    # Количество элементов на странице
    page_size_query_param = "page_size"
