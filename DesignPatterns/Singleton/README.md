# Singelaton
A Singleton pattern in Python is a design pattern that allows you to create just one instance of a class, throughout the lifetime of a program. 

## Example
```
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

Let’s create a simple module-level singleton where the data is shared among other modules. Here we will create three python files – [example_singleton.py](example_singleton.py), [sample_module1.py](./sample_module1.py), and [sample_module2.py](./sample_module2.py) – in which the other sample modules share a variable from singleton.py. 

```
# singleton.py
shared_variable = "Shared Variable"
```

```
# sample_module1.py
import example_singleton as singleton

print(singleton.shared_variable)
singleton.shared_variable += "(modified by samplemodule1)"
```

```
# sample_module2.py
import example_singleton as singleton

print(singleton.shared_variable)
```

Now run the both scripts in same Python session. Example to do so.
```
# singleton_main.py
import sample_module1
import sample_module2
```

Now run the command below.
```
python3 singleton_main.py
```

#### Output
```
Shared Variable
Shared Variable(modified by samplemodule1)
```

The first line is from `sample_module1.py`, and the second line is from `sample_module2.py` after modifying the variable `shared_variable` in `sample_module1.py`.

Here, the value changed by **sample_module1** is also reflected in **sample_module2**.

### Classic Singleton
Classic Singleton creates an instance only if there is no instance created so far; otherwise, it will return the instance that is already created.



#### References
- [GeekforGeeks](https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/)