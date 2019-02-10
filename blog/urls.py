import xadmin
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

# app -> views
from articles.views import ArticlesListViewSet, ArticlesCategoryViewSet, ArchiveApiView

# 配置router -> urls
router = DefaultRouter()
router.register(r'articles', ArticlesListViewSet)
router.register(r'category', ArticlesCategoryViewSet)

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^archive/', ArchiveApiView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # json-api
    url(r'^', include(router.urls)),

    url(r'docs/', include_docs_urls(title='博客'))
]
