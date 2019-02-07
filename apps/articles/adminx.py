import xadmin
from .models import Articles

class ArticlesAdmin(object):
    list_display = ['title', 'content', 'category', 'add_time', "update_time", 'click_count', 'comment_count']
    list_editable = ['title', 'content', 'category', "update_time"]
    search_fields = ['title']

xadmin.site.register(Articles, ArticlesAdmin)