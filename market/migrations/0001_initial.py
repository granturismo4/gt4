# Generated by Django 3.0.8 on 2020-07-12 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.IntegerField()),
                ('car_photo', models.ImageField(upload_to='cars/')),
                ('car_price', models.IntegerField()),
            ],
        ),
    ]
