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
