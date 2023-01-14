## Django Nest Multivendor Redevelop
Re-develop django nest multivendor

Github link: https://github.com/gurnitha/django-nest-multivendor-redevelop


## 01. Setup


#### 01.1 Modified read and .gitignore files

        modified:   .gitignore
        modified:   README.md


#### 01.2 Create virtual environment and install django


        F:\_workspace\ytb-desphixs\django-nest-multivendor-redevelop (main)
        λ python -m venv venv3941
        λ venv3941\Scripts\activate.bat
        (venv3941) λ pip install django
        Collecting django
          Using cached Django-4.1.5-py3-none-any.whl (8.1 MB)
        ...
        (venv3941) λ python.exe -m pip install --upgrade pip

        modified:   README.md


## 02. Creating Django Project and Application


#### 02.1 Create project named 'config'

        (venv3941) λ django-admin startproject config .

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 02.2 Create app inside app folder called 'home'

        (venv3941) λ mkdir app\home
        (venv3941) λ django-admin startapp home app\home

        modified:   README.md
        new file:   app/home/__init__.py
        new file:   app/home/admin.py
        new file:   app/home/apps.py
        new file:   app/home/migrations/__init__.py
        new file:   app/home/models.py
        new file:   app/home/tests.py
        new file:   app/home/views.py
        modified:   config/settings.py

        Aktivities:

        1. Create app
        2. Rename the app name in apps.py:
           from: name='home'
           to  : name='app.home'
        3. Register the app to config
        4. Run the server


## 03. Building The Homepage


#### 03.1 Create homepage

        Activities:		

        modified:   README.md
        new file:   app/home/urls.py
        1. Create urls.py file and define the home path
        modified:   app/home/views.py
        2. Define home_page method
        modified:   config/settings.py
        3. Activate django template and import os
        modified:   config/urls.py
        4. Include the home's urls.py 
        new file:   templates/app/home/index.html
        5. Create templates/home and index.html


#### 03.3 Add html template to homepage

        Activities:

        modified:   README.md
        modified:   templates/app/home/index.html
        1. Adding html template


#### 03.4 Adding and loading static files

        Activities:

        modified:   README.md
        modified:   config/settings.py
        1. Activated django templates:'DIRS': [os.path.join(BASE_DIR, 'templates')],
        2. Setting up static files path:
	        # New: Setup static files
	        STATIC_URL = '/static/'
	        STATIC_ROOT = BASE_DIR /'static'
	        STATICFILES_DIRS = [
	        	'config/static'
	        ]
        modified:   templates/app/home/index.html
        3. Loading static files ie:
        	<link rel="stylesheet" href="{% static 'assets/css/main.css' %}" />
        	url({% static 'assets/imgs/banner/popup-1.png' %})"


#### 03.5 Templates inheritance - Part 1: Creating base template 

        Activities:

        modified:   README.md
        modified:   templates/app/home/index.html
        1. Fixing tiny error of loading static file
        new file:   templates/base.html
        2. Creating base.html template and extends it to index.html


#### 03.6 Templates inheritance - Part 2: Partials and Include  

        new file:   templates/app/home/inc/banner.html
        new file:   templates/app/home/inc/daily-best-sells.html
        new file:   templates/app/home/inc/deals-of-the-day.html
        new file:   templates/app/home/inc/featured-categories.html
        new file:   templates/app/home/inc/popular-products.html
        new file:   templates/app/home/inc/slider-hero.html
        new file:   templates/app/home/inc/top-selling.html
        modified:   templates/app/home/index.html
        modified:   templates/base.html
        new file:   templates/partials/footer.html
        new file:   templates/partials/header-logo.html
        new file:   templates/partials/header-nav-bar.html
        new file:   templates/partials/header-nav-mobile.html
        new file:   templates/partials/header-top.html
        new file:   templates/partials/header.html
        new file:   templates/partials/modal.html
        new file:   templates/partials/quick-view.html


#### 03. Create Carousel model

        Activities:

        modified:   app/home/models.py  
        1. Create Carousel model:
        # MODEL:
        class Carousel(models.Model):
        image = models.ImageField(upload_to='images/carousel', default='carousel.png')
        title = models.CharField(max_length=200)
        car_url = models.CharField(max_length=200)

        new file:   app/home/migrations/0001_initial.py
        2. Run adn apply migrations
        modified:   app/home/admin.py
        3. Register Carousel model to admin


#### 04. Creating superuser

        (venv3941) λ python manage.py createsuperuser
        Username (leave blank to use 'hp'): admin
        Email address: admin@admin.com
        Password: admin
        Password (again): admin
        The password is too similar to the username.
        This password is too short. It must contain at least 8 characters.
        This password is too common.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.


#### 04. Rendering Carousels

        modified:   README.md
        modified:   app/home/views.py
        1. Get all carousels instance
        modified:   config/settings.py
        2. Setup media files 
        modified:   config/urls.py
        3. Add path for media files and static files
        new file:   images/carousel/slider-1.png
        new file:   images/carousel/slider-2.png
        new file:   media/images/carousel/slider-1.png
        new file:   media/images/carousel/slider-2.png
        modified:   templates/app/home/inc/slider-hero.html
        4. Load/loop slider instance 

        NOTE: Carousel title is too long, cant break it using <br>

        NEXT: Create title in two field (first_part, second_part)


#### 05. Rendering Carousels with 2 title fields

        modified:   app/home/models.py
        1. Modified the Carousel model with this:
        title_first_part = models.CharField(max_length=20)
        title_second_part = models.CharField(max_length=30)
        new file:   app/home/migrations/0002_remove_carousel_title_carousel_title_first_part_and_more.py
        2. Run and apply migrations
        modified:   app/home/views.py
        3. Comment this part:
        # print(carousels)
        modified:   templates/app/home/inc/slider-hero.html
        4. Render the carousel to homepage

        NEXT: Subscribe


#### 06. Subscribe 

        modified:   app/home/models.py
        1. Define Subscribe model, like this:
        class Subscribe(models.Model):
        email = models.EmailField(max_length=100)
        date  = models.DateTimeField(auto_now=True)
        new file:   app/home/migrations/0003_subscribe.py
        2. Run and apply migrations
        new file:   app/home/forms.py
        3. Create SubscribeForm form model, like this:
        from django import forms
        from django.utils.translation import gettext_lazy as _

        # Import from locals
        from app.home.models import Subscribe

        class SubscribeForm(forms.ModelForm):
        class Meta:
        model=Subscribe
        fields='__all__'
        labels = {'email':_('')}

        def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        modified:   app/home/admin.py
        4. Register Subscribe model to admin
        modified:   app/home/views.py
        5. Define logic in home_page view method, like this:
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
        modified:   templates/app/home/inc/slider-hero.html
        6. Render subscribe_form to homepage, like this:
        <form method="post" class="form-subcriber d-flex">
        {% csrf_token %}
        {{subscribe_form}}

        <button class="btn" type="submit">Subscribe</button>
        </form>
        {% if subscribe_successfull %}
        <br><p>Subscribed successfully!</p>
        {% endif %}

        NOTE: It worked, saved the subscriber data to db:)