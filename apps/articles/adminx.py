import xadmin
from .models import Articles, ArticlesCategory


class ArticlesAdmin(object):
    list_display = ['title', 'content', 'category', 'add_time', "update_time", 'click_count', 'comment_count']
    list_editable = ['title', 'content', 'category', "update_time"]
    search_fields = ['title']


class ArticlesCategoryAdmin(object):
    list_display = ['name', 'index', 'desc', 'is_active', 'parent_category']
    search_fields = ['name']


xadmin.site.register(ArticlesCategory, ArticlesCategoryAdmin)
xadmin.site.register(Articles, ArticlesAdmin)
