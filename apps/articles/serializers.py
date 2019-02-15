from rest_framework import serializers
from .models import Articles, ArticlesCategory


class ArticlesCategorySerializer2(serializers.ModelSerializer):
    class Meta:
        model = ArticlesCategory
        fields = "__all__"


class ArticlesCategorySerializer(serializers.ModelSerializer):
    """文章类别序列化"""
    sub_category = ArticlesCategorySerializer2(many=True)

    class Meta:
        model = ArticlesCategory
        fields = "__all__"


class ArticlesSerializer(serializers.ModelSerializer):
    category = ArticlesCategorySerializer()

    class Meta:
        model = Articles
        fields = ('id', 'title', 'category', 'content', 'add_time', 'update_time')  # "__all__"
