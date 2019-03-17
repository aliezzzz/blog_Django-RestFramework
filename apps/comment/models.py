from django.db import models
from users.models import UserProfile
from articles.models import Articles


# Create your models here.
class Comment(models.Model):
    """
    文章
    """
    author = models.ForeignKey(UserProfile, null=True, blank=True, related_name="comments", verbose_name='作者', on_delete=models.SET_NULL)
    post = models.ForeignKey(Articles, null=False, blank=False, verbose_name='所属文章', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=30, default='', verbose_name="用户名")
    author_avatar = models.CharField(max_length=200, default='', verbose_name="作者头像")
    content = models.TextField(null=False, blank=True, verbose_name="内容")
    status = models.BooleanField(default=True, verbose_name="是否激活", help_text="激活状态")
    is_recommend = models.BooleanField(default=False, verbose_name="是否推荐", help_text="是否推荐")
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="添加时间")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

