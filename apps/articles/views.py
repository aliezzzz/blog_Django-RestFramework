from rest_framework import mixins, generics, status, viewsets, filters
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Articles, ArticlesCategory
from .serializers import ArticlesSerializer, ArticlesCategorySerializer
from .filters import ArticlesFilter


class ArticlesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


# class ArticlesListView(generics.ListAPIView):
class ArticlesListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    文章列表api
    """
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    pagination_class = ArticlesPagination
    # django_filters
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title', 'content')
    ordering_fields = ('add_time', 'update_time')
    filter_class = ArticlesFilter


class ArticlesCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    文章分类列表数据
    """
    queryset = ArticlesCategory.objects.filter()
    serializer_class = ArticlesCategorySerializer


class ArchiveApiView(APIView):

    def get(self, request):
        date_dict = Articles.objects.distinct_date()
        return Response(date_dict)

