# Generated by Django 2.1.5 on 2019-02-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190205_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailverifyrecord',
            options={'verbose_name': '邮箱验证码', 'verbose_name_plural': '邮箱验证码'},
        ),
        migrations.RemoveField(
            model_name='emailverifyrecord',
            name='add_time',
        ),
        migrations.AddField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(auto_now_add=True, help_text='发送时间', null=True, verbose_name='发送时间'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='code',
            field=models.CharField(help_text='验证码', max_length=20, verbose_name='验证码'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='email',
            field=models.EmailField(help_text='邮箱', max_length=50, verbose_name='邮箱'),
        ),
    ]
