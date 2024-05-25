# manage.py

`manage.py` is a command-line utility in `Django` that allows you to interact with your Django project in various ways. 

Here are some key points about manage.py:

### Purpose:
- When you create a new Django project using the startproject command, a Python script called `manage.py` is automatically generated.
- It resides in the root directory of your project.

### Functionality:
- `manage.py` provides several useful commands for managing your Django project.
- Running the development server (`runserver`)
- Creating database tables (`migrate`)
- Creating a new app (`startapp`)
- Running tests (`test`)
- And more!

### Custom Commands:
- You can also create custom management commands using `manage.py`.
- These custom commands allow you to perform specific tasks related to your project.
- To create custom commands, use the `management/commands` directory and define a Python class that inherits from `BaseCommand`.

#### References
- [`django-admin` and `manage.py`](https://docs.djangoproject.com/en/5.0/ref/django-admin/)