# Generated by Django 5.1.4 on 2024-12-11 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='slug',
            field=models.SlugField(default='none'),
            preserve_default=False,
        ),
    ]
