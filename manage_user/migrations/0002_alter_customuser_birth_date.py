# Generated by Django 4.2.2 on 2023-06-22 09:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manage_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]