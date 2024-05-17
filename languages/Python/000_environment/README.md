# Virtual Environment
A virtual environment in Python is an isolated, self-contained workspace where you can work on your Python projects separately from your system-installed Python.

- A virtual environment ensures that the Python interpreter, libraries, and scripts installed within it are isolated from those in other virtual environments and the system-wide Python installation.
- By default, any libraries installed in a system Python won’t interfere with those in your virtual environment.
- Virtual environments allow you to maintain project-specific dependencies and configurations.
- You can create separate environments for different projects, ensuring that packages installed for one project don’t affect others.
- It’s especially useful when working on multiple projects with different requirements.

## Create and Activate
### Windows
Create
```
py -m venv my_virtual_env_name
```

Activate
```
my_virtual_env_name\Scripts\activate
```
### Unix/MacOS

Create
```
python -m venv my_virtual_env_name
```

Activate
```
source my_virtual_env_name/bin/activate
```

---
> **_NOTE:_**
`Python` command may not found on some **OS**, there if `Python` is installed then used `Python3` instead of `Python`.
---

### Study materisl
- [Python Docs](https://python.readthedocs.io/en/stable/library/venv.html)
- [RealPython](https://realpython.com/python-virtual-environments-a-primer/)
