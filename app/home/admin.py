# app/home/urls.py

# Import django modules
from django.contrib import admin

# Import from locals
from app.home.models import Carousel, Subscribe

# Registering site
admin.site.register(Carousel)
admin.site.register(Subscribe)