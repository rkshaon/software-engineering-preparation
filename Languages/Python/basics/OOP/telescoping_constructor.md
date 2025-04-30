# Telescoping Constructor
**Telescoping constructors** refer to a pattern where a class has ***multiple constructors with increasing numbers of parameters***, to handle different combinations of object initialization.

## Example
```python
class User:
    def __init__(self, name):
        pass

    def __init__(self, name, age):
        pass

    def __init__(self, name, age, address):
        pass
```

This becomes **hard to manage**, especially when parameters are optional or have defaults — that's where the **[Builder Pattern](../../../../DesignPatterns/CreationalPatterns/Builder/README.md)** shines as a cleaner solution.
