# Generated by Django 4.2.2 on 2023-07-14 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_tours', '0019_remove_itinerary_tour_tour_itinerary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='tour',
        ),
        migrations.AddField(
            model_name='tour',
            name='faq',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manage_tours.faq', verbose_name='سوالات متداول'),
        ),
    ]