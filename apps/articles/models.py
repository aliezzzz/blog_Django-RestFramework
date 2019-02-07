from django.db import models
from django.contrib.auth.models import AbstractUser


class ArticlesCategory(models.Model):
    """
    文章分类
    """
    index = models.IntegerField(default=0, verbose_name="排序", help_text="排序")
    name = models.CharField(max_length=30, default="", verbose_name="类别名", help_text="类别名")
    desc = models.TextField(null=True, blank=True, verbose_name="类别描述", help_text="类别描述")
    is_active = models.BooleanField(default=True, verbose_name="是否激活", help_text="是否激活")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Articles(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=100, default='', blank=False, null=False, verbose_name='标题')
    content = models.TextField(null=False, blank=True, verbose_name="内容")
    category = models.ForeignKey(ArticlesCategory, null=False, blank=False, default='', on_delete=models.CASCADE, verbose_name="类别")
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="添加时间")
    update_time = models.DateTimeField(null=True, blank=True, verbose_name="修改时间")
    click_count = models.IntegerField(default=0, verbose_name="点击量")
    comment_count = models.IntegerField(default=0, verbose_name="评论数")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

