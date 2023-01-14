# app/home/views.py

# Import django modules
from django.shortcuts import render

# Import from locals
from app.home.models import (
	Carousel, HeadTextAd, HomeAdDayly, 
	HomeAdDealTime, HomeAdMiddleBanner)
from app.home.forms import SubscribeForm

# VIEWS: home
def home_page(request):
	carousels = Carousel.objects.all()
	# print(carousels)
	head_text_ads = HeadTextAd.objects.all()
	home_ad_daylies = HomeAdDayly.objects.all()
	home_ad_deal_times = HomeAdDealTime.objects.all()
	home_ad_mid_banners = HomeAdMiddleBanner.objects.all()

	# Subscription
	subscribe_form = SubscribeForm()
	subscribe_successfull = None

	if request.POST:
		subscribe_form = SubscribeForm(request.POST)
		if subscribe_form.is_valid():
			subscribe_form.save()
			subscribe_successfull = 'Subscribed successfully.'
			subscribe_form = SubscribeForm()

	context = {
		'carousels':carousels,
		'subscribe_form':subscribe_form,
		'subscribe_successfull':subscribe_successfull,
		'head_text_ads':head_text_ads,
		'home_ad_daylies':home_ad_daylies,
		'home_ad_deal_times':home_ad_deal_times,
		'home_ad_mid_banners':home_ad_mid_banners,
	}
	return render(request, 'app/home/index.html', context)