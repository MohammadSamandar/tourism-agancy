# Generated by Django 4.2.2 on 2023-07-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_tours', '0005_tour_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=200, unique=True),
        ),
    ]
