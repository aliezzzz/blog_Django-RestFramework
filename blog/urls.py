import xadmin
from django.conf.urls import url, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from blog.settings import MEDIA_ROOT

# app -> views
from articles.views import ArticlesListViewSet, ArticlesCategoryViewSet, ArchiveApiView, ArticleRssFeed
from users.views import EmailCodeViewSet, RegisterViewSet
from comment.views import CommentViewSet, CommentListViewSet

# 配置router -> urls
router = DefaultRouter()
router.register(r'articles', ArticlesListViewSet, base_name="articles")
router.register(r'category', ArticlesCategoryViewSet, base_name="category")
router.register(r'code', EmailCodeViewSet, base_name="code")
router.register(r'register', RegisterViewSet, base_name="register")
router.register(r'comment', CommentViewSet, base_name="comment")
router.register(r'commentList', CommentListViewSet, base_name="commentList")

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^froala_editor/', include('froala_editor.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 获取媒体路径

    # json-api
    url(r'^', include(router.urls)),
    url(r'^archive/', ArchiveApiView.as_view()),
    url(r'^rss/$', ArticleRssFeed(), name='rss'),
    # # drf自带的认证模式
    # url(r'^login/', views.obtain_auth_token),
    # jwt的认证接口
    url(r'^login/', obtain_jwt_token),

    url(r'docs/', include_docs_urls(title='博客'))
]



