# The get() Method on Dictionaries and its "Default" Argument
In Python, the `get()` method is used to retrieve the value for a given key from a dictionary. If the key is not found, `get()` returns a default value instead of raising a `KeyError`. This feature makes it a useful tool for situations where you want to provide a fallback option when a key is missing.

## Example
```python
# The get() method on dicts and its "default" argument

name_for_userid = {
    382: "Rezaul",
    590: "Karim",
    951: "Shaon",
}


def greeting(userid: int = None):
    return "Hi %s!" % name_for_userid.get(userid, "there")


print(greeting(382))        # "Hi Alice!"
print(greeting(333333))     # "Hi there!"
print(greeting())           # "Hi there!"
```

## Explanation
### Dictionary Setup
- Created a dictionary `name_for_userid` where keys are user IDs (`int`), and values are names (`str`).
- Example: `382` maps to `"Rezaul"`, `590` maps to `"Karim"`, and `951` maps to `"Shaon"`.

### Function Definition
- Defined a function `greeting(userid: int = None)` that takes an optional `userid` argument of type `int`. If no `userid` is provided, it defaults to `None`.
- Inside the function, the `get()` method is used on the `name_for_userid` dictionary to retrieve the name associated with the provided `userid`.
- The `get()` method is called as `name_for_userid.get(userid, "there")`.
    - If the `userid` exists in the dictionary, the corresponding name is returned.
    - If the `userid` does not exist or is None, the default value `"there"` is returned.

### Function Calls and Outputs
- `greeting(382)`
    - The `userid` `382` exists in the dictionary and maps to `"Rezaul"`.
    - The function returns `"Hi Rezaul!"`.
- `greeting(333333)`
    - The `userid` `333333` does not exist in the dictionary.
    - The `get()` method returns the default value `"there"`.
    - The function returns "Hi there!".
- `greeting()`
    - No `userid` is provided, so the default argument `None` is used.
    - The `get()` method does not find None in the dictionary, so it returns the default value `"there"`.
    - The function returns `"Hi there!"`.

## Summary
The `get()` method on dictionaries is a powerful tool for safely accessing dictionary values without risking a `KeyError`. By providing a default value, as shown in the example above, you can handle missing keys gracefully, ensuring your code remains robust and user-friendly.
