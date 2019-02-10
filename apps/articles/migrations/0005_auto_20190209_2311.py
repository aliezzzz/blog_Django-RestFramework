# Generated by Django 2.1.5 on 2019-02-09 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_articlescategory_parent_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='pub_time',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='articlescategory',
            name='index',
            field=models.IntegerField(auto_created=True, default=0, help_text='排序', unique=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='articlescategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_category', to='articles.ArticlesCategory', verbose_name='父类目级别'),
        ),
    ]