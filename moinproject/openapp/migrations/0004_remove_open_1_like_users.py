# Generated by Django 3.2.2 on 2021-11-02 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openapp', '0003_open_1_like_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='open_1',
            name='like_users',
        ),
    ]