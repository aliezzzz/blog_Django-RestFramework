from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from rest_framework import status


from .models import Articles
from .serializers import ArticlesSerializer


class ArticlesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100

class ArticlesListView(generics.ListAPIView):
    """
    文章列表api
    """
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    pagination_class = ArticlesPagination

