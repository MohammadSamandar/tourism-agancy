# Generated by Django 4.2.2 on 2023-07-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_tours', '0006_tour_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/tour-image', verbose_name='تصویر اصلی'),
        ),
    ]