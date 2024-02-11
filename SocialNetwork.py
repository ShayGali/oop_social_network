from typing import Dict, Set

from User import User


class SocialNetwork:
    instance = None

    @staticmethod
    def get_instance():
        return SocialNetwork.instance

    # TODO: singleton
    def __init__(self, name: str):
        self.name = name
        self.users: Dict[str, User] = dict()
        self.logged_in_users: Set[User] = set()

        print(f"The social network {name} was created!")
        SocialNetwork.instance = self

    def sign_up(self, username: str, password: str) -> User:
        if username in self.users:
            raise ValueError("Username already exists")  # TODO: check if this is the right way to do it

        user = User(username, password)
        self.users[username] = user
        self.logged_in_users.add(user)
        return user

    def log_out(self, username: str) -> None:
        # TODO: check if need this if statement
        if username not in self.users:
            raise ValueError("Username does not exist")

        # TODO: check if need this if statement
        if self.users[username] not in self.logged_in_users:
            raise ValueError("User is not logged in")

        # remove user from logged_in_users
        self.logged_in_users.remove(self.users[username])
        print(f"{username} disconnected")

    def log_in(self, username: str, password: str) -> None:
        if username not in self.users:
            raise ValueError("Username does not exist")

        user = self.users[username]
        if user.password != password:
            raise ValueError("Password is incorrect")

        self.logged_in_users.add(user)
        print(f"{username} connected")
        # TODO: what to do if the user is already logged in?

    def is_user_logged_in(self, user: User) -> bool:
        return user in self.logged_in_users

    def __str__(self):
        users = "\n".join([str(u) for u in self.users.values()])
        return f'{self.name} social network:\n{users}'

    def __repr__(self):
        return self.__str__()
