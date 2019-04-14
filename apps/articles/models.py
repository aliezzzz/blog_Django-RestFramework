from django.db import models
from django.contrib.auth.models import AbstractUser
from froala_editor.fields import FroalaField


class ArticlesCategory(models.Model):
    """
    分类
    """
    CATEGORY_LEVEL = (
        ("1", "一级类目"),
        ("2", "二级类目")
    )
    index = models.IntegerField(unique=True, auto_created=True, verbose_name="排序", help_text="排序")
    cate_level = models.CharField(max_length=10, default='', choices=CATEGORY_LEVEL, verbose_name="分类级别", help_text="分类级别")
    name = models.CharField(max_length=30, default="", verbose_name="分类名", help_text="分类名")
    is_active = models.BooleanField(default=True, verbose_name="是否激活", help_text="是否激活")
    # 此处的limit_choices_to 参数 指定的是 只有满足条件的选项才能成为外键
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_category", on_delete=models.SET_NULL,
                                        limit_choices_to={'cate_level': 1})

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# class ArticlesManager(models.Manager):
#     def distinct_date(self):
#         distinct_date_list = []
#         mark_list = []
#         date_list = self.values('add_time')
#         for date in date_list:
#             datetime = date['add_time'].strftime('%Y-%m')
#             dict_index = 0
#             if datetime not in mark_list:
#                 mark_list.append(datetime)
#                 distinct_date_list.append({'date': datetime, 'count': 1})
#             else:
#                 distinct_date_list[dict_index]['count'] += 1
#             dict_index += 1
#         return distinct_date_list


# 现在函数的写法 时间必须按正常排序 不能混序
class ArticlesManager(models.Manager):
    def distinct_date(self):
        distinct_date_dic = []
        mark_list = []
        mark_year = ''
        dict_index = -1
        date_list = self.values('add_time')
        print(date_list)
        for date in date_list:
            year = date['add_time'].strftime('%Y')
            datetime = date['add_time'].strftime('%Y-%m')
            print(datetime)
            if mark_year != year:
                distinct_date_dic.append({year: []})
                mark_year = year
                dict_index = -1
            if datetime not in mark_list:
                distinct_date_dic[-1][year].append({'date': datetime, 'count': 1})
                print(distinct_date_dic)
                dict_index += 1
                mark_list.append(datetime)
            else:
                print(dict_index)
                print(distinct_date_dic[-1])
                distinct_date_dic[-1][year][dict_index]['count'] += 1
        return distinct_date_dic

    # def distinct_date(self):
    #     distinct_date_dic = {}
    #     mark_list = []
    #     mark_year = ''
    #     dict_index = -1
    #     date_list = self.values('add_time')
    #     for date in date_list:
    #         year = date['add_time'].strftime('%Y')
    #         datetime = date['add_time'].strftime('%Y-%m')
    #         print(datetime)
    #         if mark_year != year:
    #             distinct_date_dic[year] = []
    #             mark_year = year
    #             dict_index = -1
    #         if datetime not in mark_list:
    #             distinct_date_dic[year].append({'date': datetime, 'count': 1})
    #             print('+++')
    #             dict_index += 1
    #             mark_list.append(datetime)
    #         else:
    #             print(dict_index)
    #             print(distinct_date_dic[year])
    #             distinct_date_dic[year][dict_index]['count'] += 1
    #     return distinct_date_dic


class Articles(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=100, default='', blank=False, null=False, verbose_name='标题')
    content = FroalaField(verbose_name="文章内容", help_text="文章内容")
    category = models.ForeignKey(ArticlesCategory, null=True, blank=True, default='', on_delete=models.SET_NULL,
                                 verbose_name="类别")
    is_active = models.BooleanField(default=True, verbose_name="是否激活", help_text="是否激活")
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="添加时间")
    update_time = models.DateTimeField(null=True, blank=True, verbose_name="修改时间")
    click_count = models.IntegerField(default=0, verbose_name="点击量")
    comment_count = models.IntegerField(default=0, verbose_name="评论数")
    objects = ArticlesManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

