# DRY
`DRY` stands for `Don’t Repeat Yourself`. It avoid code duplication, eliminate redundancy in code and processes.

#### Bad Example
```
def calculate_area_of_rectangle(length, width):
    return length * width


def calculate_area_of_square(side):
    return side * side

```
#### Good Example
```
def calculate_area(length, width):
    return length * width

```

Repeating the same code or logic in multiple places leads to maintenance nightmares. Instead, centralize common functionality to a single location.

### Interesting Article on DRY
- [`Dont Repeate Yourself` on *wiki.c2.com*](./wiki.c2.com.md)