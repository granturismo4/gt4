# Generated by Django 3.0.8 on 2020-07-31 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0016_auto_20200729_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_nickname',
            field=models.CharField(default='', max_length=100),
        ),
    ]
