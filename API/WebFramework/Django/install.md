# Install Django

To install Django, it is required to have Python installed. And it is good to have a virtual environment.

To know how to create and activate virtual environment on Windows or Unix/MacOS [click here](../../../Languages/Python/000_environment/README.md).

#### Install Django using PIP
```
pip install Django
```
This will install the latest version of Django.

If you want to install a specific version of Django, then you have to mention version number like below.
```
pip install Django==2.0.1
```

See all Django releases see [here](https://pypi.org/project/Django/) or [here](https://docs.djangoproject.com/en/5.0/releases/)

After installing Django, let's check the version.
#### Unix/MacOS
```
python -m django --version
```

#### Windows
```
py -m django --version
```

#### References
- [Django Doc](https://docs.djangoproject.com/en/5.0/topics/install/)