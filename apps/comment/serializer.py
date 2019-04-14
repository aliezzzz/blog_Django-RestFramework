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
        userModel = validated_data["author"]
        validated_data["author_name"] = userModel.username
        validated_data["author_avatar"] = userModel.avatar

        post_id = validated_data["post"]
        post = Articles.objects.get(id=post_id)  # 取得对应的articles
        post.comment_count += 1  # 增加点击量
        post.save()
        validated_data["post"] = post
        instance = self.Meta.model._default_manager.create(**validated_data)  # create 数据
        return instance

    class Meta:
        model = Comment
        fields = ("author", "author_name", "post", "id", "content", "add_time", "status")
