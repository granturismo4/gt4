# Generated by Django 3.0.8 on 2020-07-19 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_cars_car_headline'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='car_boughtat',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
