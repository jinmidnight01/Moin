# Generated by Django 3.2.2 on 2021-11-03 08:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openapp', '0004_remove_open_1_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='open_1',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='open_1',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]