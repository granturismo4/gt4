# Generated by Django 3.0.8 on 2020-07-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0013_auto_20200729_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='car_power',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cars',
            name='car_rank',
            field=models.IntegerField(default=0),
        ),
    ]
