# Generated by Django 4.2.6 on 2024-01-16 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_apartment_lat_apartment_long_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='num_guests',
            field=models.IntegerField(default=0),
        ),
    ]
