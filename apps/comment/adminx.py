import xadmin
from .models import Comment


class CommentAdmin(object):
    list_display = ['author_name', 'content', 'post', 'status', 'is_recommend', 'add_time']
    search_fields = ['author_name', 'content']


xadmin.site.register(Comment, CommentAdmin)
