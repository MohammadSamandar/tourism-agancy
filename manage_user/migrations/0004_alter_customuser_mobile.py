# Generated by Django 4.2.2 on 2023-07-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_user', '0003_customuser_email_active_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]