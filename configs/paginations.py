from rest_framework import pagination
from rest_framework.response import Response
from collections import OrderedDict


class CustomPagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'pageSize'
    max_page_size = 10000

    def paginate_queryset(self, queryset, request, view=None):
        # Nếu có tham số noPagination=true, không phân trang
        if request.query_params.get('noPagination', 'false').lower() == 'true':
            return None
        return super().paginate_queryset(queryset, request, view)
    
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'results': data
        })

