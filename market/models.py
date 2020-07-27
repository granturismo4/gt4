from django.db import models


class Cars(models.Model):
    car_id = models.IntegerField()
    car_headline = models.CharField(max_length=100, default='')
    car_year_name = models.CharField(max_length=100, default='')
    car_photo = models.ImageField(upload_to='cars/')
    car_description = models.CharField(max_length=1000, default='')
    car_price = models.FloatField()
    car_forsale = models.CharField(max_length=5, default="off")
    car_boughtat = models.DateTimeField()

    def __str__(self):
        return self.car_year_name
