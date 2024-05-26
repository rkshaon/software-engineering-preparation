# Tip 2: Specify function argument types and return types

## Bad practice
- Not specifying argument types
- Not specifying return types

## Good practice
- Specify argument types
- Specify return types


### Example
```
def get_users():
    users = {
        1: "Rezaul",
        2: "Karim",
        3: "Shaon",
    }
    return users

def display_users(users):
    for user_id, user_name in users.items():
        print(f"{user_id}: {user_name}")

def main():
    users = get_users()
    display_users(users)

if __name__ == "__main__":
    main()

```
Not specifying argument types and return types can lead to confusion and errors.
```
def get_users() -> dict[int, str]:
    users: dict[int, str] = {
        1: "Rezaul",
        2: "Karim",
        3: "Shaon",
    }
    return users

def display_users(users: dict[int, str]) -> None:
    for user_id, user_name in users.items():
        print(f"{user_id}: {user_name}")

def main() -> None:
    users: dict[int, str] = get_users()
    display_users(users)

if __name__ == "__main__":
    main()
```
Specifying argument types and return types can improve the clarity, error handling, and maintainability of your code.

## Benefits
- Clarity
- Error Handling
- Maintainability
- Increase code quality
- Decrease risk of bugs and errors
- Enhanced Tooling Support
- Improved Collaboration
- Refactoring Confidence
- Documentation and Self-Documentation