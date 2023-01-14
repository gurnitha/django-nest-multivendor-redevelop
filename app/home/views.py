# app/home/views.py

# Import django modules
from django.shortcuts import render


# VIEWS: home
def home_page(request):
	return render(request, 'app/home/index.html')