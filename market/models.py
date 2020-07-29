from django.db import models


class Cars(models.Model):

    # Basic Data
    car_id = models.IntegerField()
    car_headline = models.CharField(max_length=200, default='')
    car_year_name = models.CharField(max_length=100, default='')
    car_photo = models.ImageField(upload_to='cars/')
    car_description = models.CharField(max_length=2000, default='')
    car_hp = models.IntegerField(default=0)
    car_price = models.FloatField()
    car_forsale = models.CharField(max_length=5, default="off")
    car_boughtat = models.DateTimeField()

    # Upgrades
    car_rank = models.IntegerField(default=0)
    car_exp = models.IntegerField(default=0)
    car_power = models.IntegerField(default=0)

    def __str__(self):
        return self.car_year_name


class Users(models.Model):

    user_wallet = models.CharField(max_length=42, default='hx0000000000000000000000000000000000000000')
    user_powerpoint = models.IntegerField(default=500)

    def __str__(self):
        return self.user_wallet