# app/home/urls.py

# Import django modules
from django.db import models
from django.utils import timezone


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

	# Defining Position Status
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


# MODEL:HomeAdDealTime
class HomeAdDealTime(models.Model):

	# Defining Supplier Status
	class Supplier(models.TextChoices):        
		SALEM = 'Salem', 'Salem'        
		PIZZA = 'Pizza', 'Pizza'
		HAMBURGER = 'Hamburger', 'Hamburger'
		DUNNER = 'Dunner', 'Dunner'

	image = models.ImageField(upload_to='images/deal_time', 
			default='deal_time_ad.png',
			help_text='Please use our recommended dimensions: 568px x 503px, 250 KB MAX')
	title = models.CharField(max_length=120)
	supplier = models.CharField(max_length=50,choices=Supplier.choices,default=Supplier.SALEM)
	supplier_url = models.CharField(max_length=400)
	price = models.DecimalField(max_digits=100, decimal_places=2, default='00')
	discount = models.DecimalField(max_digits=100, decimal_places=2, default='00')
	deal_time = models.DateTimeField(default=timezone.now)


# MODEL:HomeAdMiddleBanner
class HomeAdMiddleBanner(models.Model):

	# Defining Position Status
	class ImagePosition(models.TextChoices):        
		LEFT = 'L', 'Left'        
		RIGHT = 'R', 'Right'
		MIDDLE = 'M', 'Middle'

	image = models.ImageField(upload_to='images/middle_banner', 
			default='middle_banner.png',
			help_text='Please use our recommended dimensions: 768px x 450px, 250 KB MAX')
	title_first_part = models.CharField(max_length=50)
	title_second_part = models.CharField(max_length=50, blank=True)
	ad_url = models.CharField(max_length=400)
	image_position = models.CharField(max_length=10,choices=ImagePosition.choices,default=ImagePosition.LEFT)