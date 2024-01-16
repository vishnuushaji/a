# Generated by Django 4.2.6 on 2024-01-16 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='lat',
            field=models.FloatField(blank=True, default=0, help_text='Latitude', null=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='long',
            field=models.FloatField(blank=True, default=0, help_text='Longitude', null=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='max_guest_allowed',
            field=models.PositiveIntegerField(default=0, help_text='Maximum guests allowed'),
        ),
    ]
