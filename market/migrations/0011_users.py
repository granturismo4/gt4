# Generated by Django 3.0.8 on 2020-07-29 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0010_auto_20200729_0622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_wallet', models.CharField(default='hx0000000000000000000000000000000000000000', max_length=42)),
                ('user_powerpoint', models.IntegerField(default=0)),
            ],
        ),
    ]
