# app/home/urls.py

# Import django modules
from django.contrib import admin

# Import from locals
from app.home.models import (
	Carousel, Subscribe, 
	HeadTextAd, HomeAdDayly,
	HomeAdDealTime, HomeAdMiddleBanner,
	HomeAdSupplier, SuperCategory,
	MainCategory, SubCategory, MiniCategory)

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


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):    
	list_display = ['name', 'slug', 'image_tag', 'super_category']
	list_filter = ['name',]    
	search_fields = ['name']    
	prepopulated_fields = {'slug': ('name',)}    
	ordering = ['created',]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):    
	list_display = ['name', 'slug', 'image_tag', 'super_category', 'main_category']
	list_filter = ['name',]    
	search_fields = ['name']    
	prepopulated_fields = {'slug': ('name',)}    
	ordering = ['created',]


@admin.register(MiniCategory)
class MiniCategoryAdmin(admin.ModelAdmin):    
	list_display = ['name', 'slug', 'image_tag', 'super_category', 'main_category', 'sub_category']
	list_filter = ['name',]    
	search_fields = ['name']    
	prepopulated_fields = {'slug': ('name',)}    
	ordering = ['created',]