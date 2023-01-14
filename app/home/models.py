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


# MODEL:HeadTextAd
class HeadTextAd(models.Model):
	title = models.CharField(max_length=100)
	ad_url = models.CharField(max_length=400)
	date  = models.DateTimeField(auto_now=True)


# MODEL:HomeAdDayly
class HomeAdDayly(models.Model):

	# Defining Blog Status
	class Position(models.TextChoices):        
		LEFT = 'L', 'Left'        
		RIGHT = 'R', 'Right'

	image = models.ImageField(upload_to='images/daily_ad', default='daily_ad.png')
	title = models.CharField(max_length=100)
	ad_url = models.CharField(max_length=400)
	# Adding a position field
	position = models.CharField(max_length=5,choices=Position.choices,default=Position.LEFT)

	class Meta:        
		verbose_name_plural='Home Ad Dayly'