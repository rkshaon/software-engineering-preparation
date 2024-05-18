# Tip 3: Use `docstring`

`Docstring` stands for documentation string. A `docstring` is a special type of comment in programming languages like Python that serves as a way to document code elements like modules, functions, classes, and methods.

## How to use
- In Python, `docstrings` are typically written using triple quotation marks (either `"""` or `'''`).
- `Docstrings` placed at the beginning of the definition of the code object.


### Example
```
def greet(name):
    """This function greets the specified person.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message for the person.
    """
    return f"Hello, {name}!"
```
[See complete example of of docstring](001__example.py)

## Benefits of Using Docstrings:

- Enhanced Code Readability
- Improved Maintainability
- Automatic Documentation Generation