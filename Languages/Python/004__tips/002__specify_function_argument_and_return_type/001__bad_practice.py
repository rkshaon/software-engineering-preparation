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
