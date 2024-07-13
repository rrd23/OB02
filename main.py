class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_access_level(self):
        return self._access_level

    def __str__(self):
        return f"User(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'

    def add_user(self, users_list, user):
        if user.get_user_id() not in [u.get_user_id() for u in users_list]:
            users_list.append(user)
            print(f"User {user.get_name()} added successfully.")
        else:
            print(f"User with ID {user.get_user_id()} already exists.")

    def remove_user(self, users_list, user_id):
        for user in users_list:
            if user.get_user_id() == user_id:
                users_list.remove(user)
                print(f"User with ID {user_id} removed successfully.")
                return
        print(f"User with ID {user_id} not found.")

    def __str__(self):
        return f"Admin(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"


# Пример использования
if __name__ == "__main__":
    users = []

    admin = Admin(1, "Анна")
    user1 = User(2, "Иван")
    user2 = User(3, "Мария")

    admin.add_user(users, user1)
    admin.add_user(users, user2)

    print("\nСписок пользователей:")
    for user in users:
        print(user)

    admin.remove_user(users, 2)

    print("\nОбновленный список пользователей:")
    for user in users:
        print(user)

    # Попытка добавить пользователя с существующим ID
    admin.add_user(users, User(3, "Петр"))

    # Попытка удалить несуществующего пользователя
    admin.remove_user(users, 4)