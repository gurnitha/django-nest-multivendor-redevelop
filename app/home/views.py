# app/home/views.py

# Import django modules
from django.shortcuts import render

# Import from locals
from app.home.models import Carousel

# VIEWS: home
def home_page(request):
	carousels = Carousel.objects.all()
	# print(carousels)
	context = {'carousels':carousels}
	return render(request, 'app/home/index.html', context)