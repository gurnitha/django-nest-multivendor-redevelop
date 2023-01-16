# app/home/urls.py

# Import django modules
from django.contrib import admin

# Import from locals
from app.home.models import (
	Carousel, Subscribe, 
	HeadTextAd, HomeAdDayly,
	HomeAdDealTime, HomeAdMiddleBanner,
	HomeAdSupplier, SuperCategory)

# Registering site
admin.site.register(Carousel)
admin.site.register(Subscribe)
admin.site.register(HeadTextAd)
admin.site.register(HomeAdDayly)
admin.site.register(HomeAdDealTime)
admin.site.register(HomeAdMiddleBanner)
admin.site.register(HomeAdSupplier)


@admin.register(SuperCategory)
class SuperCategoryAdmin(admin.ModelAdmin):    
	list_display = ['name', 'slug', 'image_tag']
	list_filter = ['name',]    
	search_fields = ['name']    
	prepopulated_fields = {'slug': ('name',)}    
	ordering = ['created',]