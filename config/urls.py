# config/urls.py

# Import django modules
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', include('app.home.urls', namespace='home')),
]
