# Generated by Django 3.0.8 on 2020-07-29 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0011_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_powerpoint',
            field=models.IntegerField(default=500),
        ),
    ]