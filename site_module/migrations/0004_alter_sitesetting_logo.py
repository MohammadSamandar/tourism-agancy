# Generated by Django 4.2.2 on 2023-07-04 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0003_alter_sitebanner_positions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='logo',
            field=models.ImageField(upload_to='images/site-logo', verbose_name='لوگو'),
        ),
    ]
