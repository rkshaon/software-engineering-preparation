# Lambda Function
Lambda function (also known as an anonymous function) is a concise way to define small, single-expression functions, often used in conjunction with higher-order functions like `map()`, `filter()`, and `sorted()`.

## Syntax
```
lambda arguments: expression
```

- `lambda`: Keyword to define a lambda function.
- `arguments`: Comma-separated list of arguments the function can accept (can be zero or more).
- `expression`: The single expression that represents the function's body. This expression is evaluated and returned when the function is called.

## Example
Add 10 to an argument
```
add_ten = lambda a: a + 10
print(add_ten(5))  # Output: 15
```

Multiply two arguments
```
multiply = lambda a, b: a * b
print(multiply(5, 6))  # Output: 30
```

Sum three arguments
```
summarize = lambda a, b, c: a + b + c
print(summarize(5, 6, 2))  # Output: 13
```

## When to Use
- `Simple, Short Operations`: When you need a small, one-line function for a quick task.
- `Higher-Order Functions`: Lambda functions are often used as arguments to higher-order functions that take functions as inputs or return functions as outputs.
- `Readability (Sometimes)`: In certain cases, lambda functions can improve code readability by keeping small logic snippets concise. However, this can be subjective and depends on the complexity of the expression.

## When to Avoid
- `Complex Logic`: If the logic you want to implement is complex and requires multiple lines or statements, using a regular def function is generally better for readability and maintainability.
- `Overuse`: Don't overuse lambda functions for the sake of brevity, as it can make code harder to understand. Use them judiciously when they genuinely enhance readability.

## Test
#### Use lambda function to verify if 2 variables summation is equal to target
[Solution](./test__001.py)