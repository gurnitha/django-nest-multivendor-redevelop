# app/home/urls.py

# Import django modules
from django.db import models


# MODEL:Carousel
class Carousel(models.Model):
	image = models.ImageField(upload_to='images/carousel', default='carousel.png')
	title_first_part = models.CharField(max_length=20)
	title_second_part = models.CharField(max_length=30)
	car_url = models.CharField(max_length=200)


# MODEL:Subscribe
class Subscribe(models.Model):
	email = models.EmailField(max_length=100)
	date  = models.DateTimeField(auto_now=True)


# MODEL:Haead_text_ads
class HeadTextAd(models.Model):
	title = models.CharField(max_length=100)
	ad_url = models.CharField(max_length=400)
	date  = models.DateTimeField(auto_now=True)
