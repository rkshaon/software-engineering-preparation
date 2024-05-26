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