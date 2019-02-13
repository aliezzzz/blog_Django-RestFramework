import xadmin
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

# app -> views
from articles.views import ArticlesListViewSet, ArticlesCategoryViewSet, ArchiveApiView
from users.views import EmailCodeViewSet, RegisterViewSet

# 配置router -> urls
router = DefaultRouter()
router.register(r'articles', ArticlesListViewSet, base_name="articles")
router.register(r'category', ArticlesCategoryViewSet, base_name="category")
router.register(r'code', EmailCodeViewSet, base_name="code")
router.register(r'register', RegisterViewSet, base_name="register")

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^archive/', ArchiveApiView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # json-api
    url(r'^', include(router.urls)),
    # # drf自带的认证模式
    # url(r'^login/', views.obtain_auth_token),
    # jwt的认证接口
    url(r'^login/', obtain_jwt_token),

    url(r'docs/', include_docs_urls(title='博客'))
]
