# Generated by Django 2.1.5 on 2019-02-14 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_count',
        ),
    ]