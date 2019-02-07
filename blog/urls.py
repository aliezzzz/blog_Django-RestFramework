# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from rest_framework.documentation import include_docs_urls

# Uncomment the next two lines to enable the admin:
import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

# from django.contrib import admin

# app -> views
from articles.views import ArticlesListView

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # json-api
    url(r'articles/$', ArticlesListView.as_view(), name='articles-list'),

    url(r'docs/', include_docs_urls(title='博客'))
]
