# Generated by Django 4.2.2 on 2023-07-05 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_tours', '0008_alter_tour_faq_alter_tour_flight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='faq',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manage_tours.faq', verbose_name='سوالات متداول'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='flight',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manage_tours.flight', verbose_name='اطلاعات پرواز'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='itinerary',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manage_tours.itinerary', verbose_name='برنامه سفر'),
        ),
    ]
