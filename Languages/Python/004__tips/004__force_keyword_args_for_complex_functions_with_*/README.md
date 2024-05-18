# Force keyword args for complex functions with *

Placing `*` at the beginning of the parameter list, it forces all subsequent arguments to be keyword arguments.

## Why force keyword arguments
- For complex functions with many parameters, it’s essential to ensure that callers provide the correct values for each parameter.
- Named parameters makes code more readable and self-documenting. This clarify which argument corresponds to which value.
- By enforcing named parameters, reduce the risk of passing incorrect values to the wrong parameters.

## How to use
- In Python 3, you can specify `keyword-only parameters` by adding an asterisk (`*`) in the function argument list.
- Parameters after the `*` are `keyword-only` and must be passed using keyword arguments.

### Example
```
from enum import Enum

class Quality(Enum):
    LOW: int = 480
    MEDIUM: int = 1080
    HIGH: int = 1440

class Privacy(Enum):
    PRIVATE: str = 'Private'
    UNLISTED: str = 'Unlisted'
    PUBLIC: str = 'Public'

def upload(file: str, *, quality: Quality, privacy: Privacy) -> None:
    print(f"Uploading: {file} in {quality.value}p ({privacy.value})")

def main() -> None:
    upload('dog.mp4', quality=Quality.HIGH, privacy=Privacy.PUBLIC)
```

## Benefits
- Improved clarity and readability
- Preventing errors
- Forcing explicitness
- Compability with default arguments
- Enforcing API stability