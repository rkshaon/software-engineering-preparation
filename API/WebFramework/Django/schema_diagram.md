# Schema Diagram or Database Diagram
A schema diagram (or database schema) is a visual representation of the structure of a database. It shows how tables are related to each other and includes the tables, columns, data types, constraints, and relationships (such as foreign keys) between tables.

## Steps to Create a Schema Diagram
- **Understand the database structure**: Before creating a schema diagram, it's important to understand the database structure, including all the tables, their columns, data types, and relationships.

- **Use a Tool or Software**: Typically used tools like ***pgAdmin*** if the database is [PostgreSQL](/Database/SQL/PostgreSQL/README.md), ***DBeaver***, or online tools like [dbdiagram.io](https://dbdiagram.io/), lightweight like [***django-extensions***](https://django-extensions.readthedocs.io/en/latest/) if the project is developed using Django.

## Creating a Schema Diagram Using Django and Graphviz
Need to have [***Graphivz***](https://graphviz.org/) package installed.

### Install
#### Linux
For Debian, Ubuntu
```
sudo apt install graphviz
sudo apt install graphviz-dev
```

For Fedora
```
sudo dnf install graphviz
```

#### Windows
[See download links](https://graphviz.org/download/)

#### MacOs
Using MacPorts
```
sudo port install graphviz
```

Using brew
```
brew install graphviz
```

#### Install on Other OS
[See here](https://graphviz.org/download/)

`graphviz-dev` package is required to generate images from `models`.

### Install Python Package
```
pip install django-extensions
pip install pygraphviz
pip install pydotplus
```

`pygraphviz` or `pydotplus` is required to generate images from `models`.

### Update Django `settings.py`
Add `django_extensions` to the `INSTALLED_APPS` in Django settings file.
```
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```

### Generate the Schema Diagram
Use the `graph_models` command provided by `django-extensions` to generate the diagram. Output of the diagram in different formats such as PNG, PDF, JSON or DOT is available.

For `png`
```
python manage.py graph_models -a -o myapp_models.png
```

For `pdf`
```
python manage.py graph_models -a -o myapp_models.pdf
```

For `dot`
```
python manage.py graph_models -a -o myapp_models.dot
```

For `json`
```
python manage.py graph_models -a -o myapp_models.json
```

Here,
- `-a`: Includes all the apps.
- `-o myapp_models.png`: Specifies the output file name and format.

#### References
- [Graphviz Download Link](https://graphviz.org/download/)
