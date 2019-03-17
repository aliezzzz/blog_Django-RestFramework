from rest_framework import mixins, generics, status, viewsets, filters
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

# RSS
from django.contrib.syndication.views import Feed
from django.urls import reverse


from .models import Articles, ArticlesCategory
from .serializers import ArticlesSerializer, ArticlesCategorySerializer
from .filters import ArticlesFilter


class ArticlesPagination(PageNumberPagination):
    page_size = 4
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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ArticlesCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    文章分类列表数据
    """
    queryset = ArticlesCategory.objects.filter(cate_level=1)
    serializer_class = ArticlesCategorySerializer


class ArchiveApiView(APIView):
    def get(self, request):
        date_dict = Articles.objects.distinct_date()
        return Response(date_dict)


class ArticleRssFeed(Feed):

    title = 'aLIEzzzz的博客'
    link = '/rss/'
    def items(self):
        return Articles.objects.all()
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.content
    def item_link(self, item):
        return "/aliezzzz.com/article" + str(item.id) + "/"
