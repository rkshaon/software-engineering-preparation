# Tip 1: use `raise NotImplementedError()` instead of `pass` or `...`

## Bad practice
- An empty function does not contain any code within it.
- It's unclear what the function is intended to do. 
- An empty function might be a placeholder during development, but it can lead to confusion and potential errors if left unaddressed.

## Good practice
- `raise NotImplementedError()` raises a NotImplementedError exception with a clear message.
- It indicates that the function is not yet implemented.


### Example
```
def test():
    pass
```
or
```
def test():
    ...
```
Keeping empty function can lead to confution and potential error.
```
def test():
    raise NotImplementedError("This function is not yet implemented.")
```
Instead using `raise NotimplemtedError()` might be helpfull for developers.

## Benefits
- Clarity
- Error Handling
- Maintainability