# app/home/urls.py

# Import django modules
from django.db import models


# MODEL:
class Carousel(models.Model):
	image = models.ImageField(upload_to='images/carousel', default='carousel.png')
	title_first_part = models.CharField(max_length=20)
	title_second_part = models.CharField(max_length=30)
	car_url = models.CharField(max_length=200)