# Create Django Project and App

## Create Project
Let's assume you have installed Django in your virtual environment.

To create Django project execute the command below.
```
django-admin startproject project_title
```
This command will create a folder named `project_title` in the current directory, under that folder the project exist.

If you want to create the project in current directory, then execute the command below.
```
django-admin startproject project_title .
```

Now you have a file named `manage.py` in the project root directory. `manage.py` is a command-line utility in Django that allows you to interact with your Django project in various ways.

To know brief about [manage.py](./manage.py.md) see the file.

## Create App
To create an application/app in the project go to the project root directory and execute the command below.
```
python manage.py startapp app_name
```
or
```
django-admin startapp app_name
```

Now you have to install the app, to do so navigate to the file `project_title/settings.py` and find the list `INSTALLED_APPS` and add the app name to the list.

Before
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
After
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_name',
]
```