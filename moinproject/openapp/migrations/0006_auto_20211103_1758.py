# Generated by Django 3.2.2 on 2021-11-03 08:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openapp', '0005_auto_20211103_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='open_2',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes_2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='open_2',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='open_3',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes_3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='open_3',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='open_4',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes_4', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='open_4',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='open_5',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes_5', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='open_5',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='open_6',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes_6', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='open_6',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='open_7',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes_7', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='open_7',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='open_8',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes_8', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='open_8',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='open_9',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes_9', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='open_9',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='open_1',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes_1', to=settings.AUTH_USER_MODEL),
        ),
    ]