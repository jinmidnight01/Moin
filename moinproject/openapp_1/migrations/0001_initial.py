# Generated by Django 3.2.6 on 2021-09-03 12:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Open_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('intro', models.CharField(max_length=200)),
                ('conent', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='openapp_1')),
                ('number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
            ],
        ),
    ]