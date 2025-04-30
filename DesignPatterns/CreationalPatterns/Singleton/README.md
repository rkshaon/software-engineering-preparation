# Singelaton
The **Singleton Pattern** ensures that ***only one instance*** of a class exists during the lifetime of an application, and it provides a ***global point of access*** to it.

**Think of it like**: _"One database connection, one logger, one configuration manager, etc."_

## ✅ Use Cases
- Database connections

- Logging services

- Caching

- Configuration management


## 💡 Core Ideas
- Private constructor so no one else can instantiate.

- A static method to return the single instance.

- Optionally, thread safety in multithreaded apps.


## Example
General example
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating the Singleton instance...")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # True
```

Example for database connection
```python
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            # Initialize the instance (e.g., establish the database connection)
            cls._instance.connection = cls._connect_to_database()
        return cls._instance

    @staticmethod
    def _connect_to_database():
        return "Database Connection Established"

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1.connection)  # Output: Database Connection Established
print(db1 is db2)  # Output: True (both references point to the same instance)
```

## Benefits of Singelaton
- To limit concurrent access to a shared resource.
- To create a global point of access for a resource.
- To create just one instance of a class, throughout the lifetime of a program.

## Implement Singelaton
A singleton pattern can be implemented in three different ways. They are as follows:

- Module-level Singleton
- Classic Singleton
- Borg Singleton

### Module Level Singelaton
All modules are singleton, by definition.

Let’s create a simple module-level singleton where the data is shared among other modules. Here we will create three python files – [example_module_singleton.py](./example_module_singleton.py), [sample_module1.py](./sample_module1.py), and [sample_module2.py](./sample_module2.py) – in which the other sample modules share a variable from singleton.py. 

```python
# singleton.py
shared_variable = "Shared Variable"
```

```python
# sample_module1.py
import example_singleton as singleton

print(singleton.shared_variable)
singleton.shared_variable += "(modified by samplemodule1)"
```

```python
# sample_module2.py
import example_singleton as singleton

print(singleton.shared_variable)
```

Now run the both scripts in same Python session. Example to do so.
```python
# singleton_main.py
import sample_module1
import sample_module2
```

Now run the command below.
```bash
python3 singleton_main.py
```

#### Output
```bash
Shared Variable
Shared Variable(modified by samplemodule1)
```

The first line is from `sample_module1.py`, and the second line is from `sample_module2.py` after modifying the variable `shared_variable` in `sample_module1.py`.

Here, the value changed by **sample_module1** is also reflected in **sample_module2**.

### Classic Singleton
Classic Singleton creates an instance only if there is no instance created so far; otherwise, it will return the instance that is already created.

```python
class SingletonClass(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(SingletonClass, cls).__new__(cls)
    
    return cls.instance


singleton = SingletonClass()
new_singleton = SingletonClass()

print(singleton is new_singleton)

singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)
```
#### Output
```bash
True
Singleton Variable
```

Here, in the `__new__` method, we will check whether an instance is created or not. If created, it will return the instance; otherwise, it will create a new instance. You can notice that singleton and new_singleton return the same instance and have the same variable.

Now, subclass a singleton class.
```python
class SingletonClass(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(SingletonClass, cls).__new__(cls)

    return cls.instance
   
class SingletonChild(SingletonClass):
    pass
   
singleton = SingletonClass()  
child = SingletonChild()
print(child is singleton)
 
singleton.singl_variable = "Singleton Variable"
print(child.singl_variable)
```

#### Output
```bash
True
Singleton Variable
```
`SingletonChild` has the same instance of `SingletonClass` and also shares the same state. But there are scenarios, where we need a different instance, but should share the same state. This state sharing can be achieved using `Borg Singleton`.

### Borg Singleton
Borg singleton is a design pattern in Python that allows state sharing for different instances.

```python
class BorgSingleton(object):
  _shared_borg_state = {}
   
  def __new__(cls, *args, **kwargs):
    obj = super(BorgSingleton, cls).__new__(cls, *args, **kwargs)
    obj.__dict__ = cls._shared_borg_state
    return obj
   
borg = BorgSingleton()
borg.shared_variable = "Shared Variable"
 
class ChildBorg(BorgSingleton):
  pass
 
childBorg = ChildBorg()
print(childBorg is borg)
print(childBorg.shared_variable)
```

#### Output
```bash
False
Shared Variable
```

The new instance creation process, a shared state is also defined in the `__new__` method. Here the shared state is retained using the shared_borg_state attribute and it is stored in the `__dict__` dictionary of each instance.

To achieve a different state, then reset the  `shared_borg_state` attribute.

```python
class BorgSingleton(object):
  _shared_borg_state = {}
   
  def __new__(cls, *args, **kwargs):
    obj = super(BorgSingleton, cls).__new__(cls, *args, **kwargs)
    obj.__dict__ = cls._shared_borg_state
    return obj
   
borg = BorgSingleton()
borg.shared_variable = "Shared Variable"
 
class NewChildBorg(BorgSingleton):
    _shared_borg_state = {}
 
newChildBorg = NewChildBorg()
print(newChildBorg.shared_variable)
```

Here the shared state is reseted and while try to access the shared_variable an error will occure.

```bash
Traceback (most recent call last):
  File "/home/329d68500c5916767fbaf351710ebb13.py", line 16, in <module>
    print(newChildBorg.shared_variable)
AttributeError: 'NewChildBorg' object has no attribute 'shared_variable'
```

#### References
- [GeekforGeeks](https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/)