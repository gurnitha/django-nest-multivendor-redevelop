# app/home/views.py

# Import django modules
from django.shortcuts import render

# Import from locals
from app.home.models import Carousel
from app.home.forms import SubscribeForm

# VIEWS: home
def home_page(request):
	carousels = Carousel.objects.all()
	# print(carousels)
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
		'subscribe_successfull':subscribe_successfull
	}
	return render(request, 'app/home/index.html', context)