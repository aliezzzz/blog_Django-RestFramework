from rest_framework import serializers
from .models import Articles, ArticlesCategory


class ArticlesCategorySerializer2(serializers.ModelSerializer):
    class Meta:
        model = ArticlesCategory
        fields = ('id', 'index', 'name', 'is_active', 'parent_category')


class ArticlesCategorySerializer(serializers.ModelSerializer):
    """文章类别序列化"""
    sub_category = ArticlesCategorySerializer2(many=True)

    class Meta:
        model = ArticlesCategory
        fields = ('id', 'index', 'name', 'is_active', 'sub_category', 'parent_category')


class ArticlesSerializer(serializers.ModelSerializer):
    # category = ArticlesCategorySerializer()
    cate_name = serializers.SerializerMethodField()

    def get_cate_name(self, articles):
        cate_dic = {}
        if not articles.category:
            return {}
        if articles.category.parent_category:
            cate_dic['category'] = articles.category.parent_category.name
            cate_dic['sub_category'] = articles.category.name
        else:
            cate_dic['category'] = articles.category.name
        return cate_dic

    class Meta:
        model = Articles
        fields = ('id', 'title', 'is_active', 'content', 'add_time', 'click_count',
                  'comment_count', 'cate_name')  # "__all__"
