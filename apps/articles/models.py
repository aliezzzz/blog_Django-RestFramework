from django.db import models
from django.contrib.auth.models import AbstractUser


class ArticlesCategory(models.Model):
    """
    文章分类
    """
    index = models.IntegerField(default=0, unique=True, auto_created=True, verbose_name="排序", help_text="排序")
    name = models.CharField(max_length=30, default="", verbose_name="类别名", help_text="类别名")
    desc = models.TextField(null=True, blank=True, verbose_name="类别描述", help_text="类别描述")
    is_active = models.BooleanField(default=True, verbose_name="是否激活", help_text="是否激活")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_category", on_delete=models.SET_NULL)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class ArticlesManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        mark_list = []
        date_list = self.values('pub_time')
        print(date_list)
        for date in date_list:
            datetime = date['pub_time'].strftime('%Y-%m')
            dict_index = 0
            if datetime not in mark_list:
                mark_list.append(datetime)
                distinct_date_list.append({'date': datetime, 'count': 1})
            else:
                distinct_date_list[dict_index]['count'] += 1
            dict_index += 1
        print(distinct_date_list)
        return distinct_date_list

class Articles(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=100, default='', blank=False, null=False, verbose_name='标题')
    content = models.TextField(null=False, blank=True, verbose_name="内容")
    category = models.ForeignKey(ArticlesCategory, null=False, blank=False, default='', on_delete=models.CASCADE,
                                 verbose_name="类别")
    is_active = models.BooleanField(default=True, verbose_name="是否激活", help_text="是否激活")
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="添加时间")
    pub_time = models.DateField(null=True, blank=True, verbose_name="添加时间")
    update_time = models.DateTimeField(null=True, blank=True, verbose_name="修改时间")
    click_count = models.IntegerField(default=0, verbose_name="点击量")
    comment_count = models.IntegerField(default=0, verbose_name="评论数")
    objects = ArticlesManager()

    # @property
    # def xxx(self):
    #     return xxxxxx

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

