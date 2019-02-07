from rest_framework import serializers
from .models import Articles, ArticlesCategory

class ArticlesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlesCategory
        fields = ('index', 'name', 'desc')

class ArticlesSerializer(serializers.ModelSerializer):
    category = ArticlesCategorySerializer()
    class Meta:
        model = Articles
        fields = ('category', 'content', 'add_time', 'update_time') # "__all__"
