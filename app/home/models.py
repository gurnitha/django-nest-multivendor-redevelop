# app/home/urls.py

# Import django modules
from django.db import models


# MODEL:
class Carousel(models.Model):
	image = models.ImageField(upload_to='images/carousel', default='carousel.png')
	title = models.CharField(max_length=200)
	car_url = models.CharField(max_length=200)