from typing import Dict, Set

from User import User

from CostomExcption import UsernameAlreadyExistsError, UserDoesNotExistError, NotLoginError, InvalidCredentialsError


class SocialNetwork:
    """
    A class representing a social network.
    The social network is a singleton.
    """
    __instance = None
    __is_initialized = False

    @staticmethod
    def get_instance():
        if SocialNetwork.__instance is None:
            raise ValueError("The social network was not created yet")
        return SocialNetwork.__instance

    def __new__(cls, name: str):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name: str):
        if self.__is_initialized:
            return  # already initialized, not need to initialize again
        self.name = name
        self.users: Dict[str, User] = dict()
        self.logged_in_users: Set[User] = set()

        self.__is_initialized = True

        print(f"The social network {name} was created!")

    def sign_up(self, username: str, password: str) -> User:
        if username in self.users:
            raise UsernameAlreadyExistsError("Username already exists")

        user = User(username, password)
        self.users[username] = user
        self.logged_in_users.add(user)
        return user

    def log_out(self, username: str) -> None:
        if username not in self.users:
            raise UserDoesNotExistError("Username does not exist")

        if self.users[username] not in self.logged_in_users:
            raise NotLoginError("Can't log out a user that is not logged in")

        # remove user from logged_in_users
        self.logged_in_users.remove(self.users[username])
        print(f"{username} disconnected")

    def log_in(self, username: str, password: str) -> None:
        if username not in self.users or self.users[username].password != password:
            raise InvalidCredentialsError("Invalid credentials")

        user = self.users[username]

        self.logged_in_users.add(user)
        print(f"{username} connected")

    def is_user_logged_in(self, user: User) -> bool:
        return user in self.logged_in_users

    def __str__(self):
        users = "\n".join([str(u) for u in self.users.values()])
        return f'{self.name} social network:\n{users}'

    def __repr__(self):
        return self.__str__()
