from typing import Set, Dict

from User import User


class Notificator:
    def __init__(self):
        self.observers: Dict[str, User] = {}


    def notify_user(self, user_to_notify: User, message: str):
        self.observers[user_to_notify.username].notify(message)

    def notify_all(self, message: str, caller: User):
        for observer in self.observers.values():
            if observer != caller:
                observer.notify(message)  # TODO: add notify method to User

    def register(self, user: User):
        self.observers[user.username] = user
