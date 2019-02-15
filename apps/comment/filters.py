import django_filters
from django.db.models import Q

from .models import Comment

import datetime


class CommentFilter(django_filters.rest_framework.FilterSet):
    """
    评论的过滤类
    """
    post = django_filters.NumberFilter(method='post_filter')

    def post_filter(self, queryset, name, value):
        return queryset.filter(post_id=value)

    class Meta:
        model = Comment
        fields = []