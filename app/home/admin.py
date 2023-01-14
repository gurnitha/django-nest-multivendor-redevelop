# app/home/urls.py

# Import django modules
from django.contrib import admin

# Import from locals
from app.home.models import Carousel

# Registering site
admin.site.register(Carousel)