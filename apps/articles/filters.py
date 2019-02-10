import django_filters
from django.db.models import Q

from .models import Articles

import datetime

class ArticlesFilter(django_filters.rest_framework.FilterSet):
    """
    文章的过滤类
    """
    time = django_filters.CharFilter(method='time_filter')
    category = django_filters.NumberFilter(method='category_filter')

    def category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value))

    def time_filter(self, queryset, name, value):
        return queryset.filter(pub_time__icontains=value)

    class Meta:
        model = Articles
        fields = []
