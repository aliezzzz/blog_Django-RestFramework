from rest_framework import serializers
from .models import Comment
from articles.models import Articles


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    post = serializers.CharField(required=True, write_only=True)

    # 传递的post是一个id 获取post_id之后，通过其取得Articles的那个对象（注意get和filter的区别）
    def create(self, validated_data):
        post = Articles.objects.get(id=validated_data["post"])
        validated_data["post"] = post
        instance = self.Meta.model._default_manager.create(**validated_data)  # create 数据
        return instance

    class Meta:
        model = Comment
        fields = ("author", "post", "id", "content")
