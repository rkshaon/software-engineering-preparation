# Use *args
When designing Python functions, it's essential to make them as flexible and versatile as possible. Using `*args` allows to create functions that can accept a variable number of positional arguments, making them more adaptable to different use cases.

## What is `*args`?
- `*args` is a special syntax in Python that allows a function to accept an arbitrary number of positional arguments.
- The name `“args”` is a convention, but it could be any valid variable name (e.g., `*values`, `*elements`, etc.).
- While defining a function with `*args` in the parameter list, it collects all the positional arguments passed to the function into a tuple.

## Use case
- `*args` is handy when you don’t know in advance how many arguments a function will receive.
- Creating generic utility functions (e.g., `sum`, `max`, `min`) that work with any number of inputs.
- Writing decorators that wrap other functions and need to handle varying argument counts.

### Example
```
def join_text(*args, sep: str) -> str:
    return sep.join(args)

def main() -> None:
    print(join_text('A', 'B', 'C', sep='-'))
    print(join_text('X', 'Y', 'Z', sep='/'))
```

## Benefits
- Flexibility
- Simplicity
- Code resuability
- Reduced / avoid repetition
- Compability
- Conciseness
- Variable length arguments
