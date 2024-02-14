from abc import ABC
from typing import Set, List

import importlib

from Notificator import Notificator


class Post(ABC):
    notificator = Notificator()

    def __init__(self, creator: "User") -> None:
        self.creator = creator
        self.likes: Set = set()  # set of users objects
        self.comments: List[("User", str)] = []

        Post.notificator.notify_all_followers(creator, f'{creator.username} has a new post')

    def like(self, user: "User") -> None:
        SocialNetwork = importlib.import_module("SocialNetwork").SocialNetwork
        # only logged in users can like
        if not SocialNetwork.get_instance().is_user_logged_in(user):
            raise ValueError("User is not logged in")

        if user not in self.likes:
            self.likes.add(user)

            Post.notificator.notify_user(self.creator, user, f'{user.username} liked your post', True)

    def comment(self, user: "User", comment: str) -> None:
        SocialNetwork = importlib.import_module("SocialNetwork").SocialNetwork
        # only logged in users can comment
        if not SocialNetwork.get_instance().is_user_logged_in(user):
            raise ValueError("User is not logged in")

        self.comments.append((user, comment))
        Post.notificator.notify_user(self.creator, user, f'{user.username} commented on your post', True, f": {comment}")

    def get_creator(self):
        return self.creator
