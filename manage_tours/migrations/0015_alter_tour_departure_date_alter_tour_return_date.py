# Generated by Django 4.2.2 on 2023-07-13 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_tours', '0014_alter_tourimagegallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='departure_date',
            field=models.DateTimeField(verbose_name='تاریخ رفت'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='return_date',
            field=models.DateTimeField(verbose_name='تاریخ برگشت'),
        ),
    ]