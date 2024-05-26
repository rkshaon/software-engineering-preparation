def get_users() -> dict[int, str]:
    """
    This function returns a dictionary of users
    consist of user_id as key and user_name as value.

    Args:
        None
    
    Returns:
        dict[int, str]: A dictionary of users.
    """
    users: dict[int, str] = {
        1: "Rezaul",
        2: "Karim",
        3: "Shaon",
    }

    return users


def display_users(users: dict[int, str]) -> None:
    """
    This function displays the users in the dictionary.

    Args:
        users: dict[int, str]: A dictionary of users.
    
    Returns:
        None
    """
    for user_id, user_name in users.items():
        print(f"{user_id}: {user_name}")


def main() -> None:
    """
    This is the main function of the program.
    It calls the get_users() 
    and display_users() functions.
    """
    users: dict[int, str] = get_users()
    display_users(users)


if __name__ == "__main__":
    main()
