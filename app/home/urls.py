# app/home/urls.py

# Import django modules
from django.urls import path

# Import from locals
from app.home import views

app_name = 'home'

urlpatterns = [
    path('', views.home_page, name='home_page'),
]
