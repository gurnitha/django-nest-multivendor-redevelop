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