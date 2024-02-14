from typing import Set, List

from PostFactory import PostFactory


# from posts.Post import Post


class User:
    def __init__(self, username: str, password: str):
        if len(password) < 4 or len(password) > 8:
            raise ValueError("Password must be 4 to 8 characters long")
        self.username = username
        self.password = password
        self.followers: Set["User"] = set()
        self.posts: List = []
        # TODO: notifications
        self.notifications: List[str] = []
        # TODO: check if it is right
        self.post_factory = PostFactory()

    def follow(self, user: "User") -> None:
        # TODO: only logged in users can follow
        if user == self:
            raise ValueError("Cannot follow yourself")  # TODO: check if need to raise an exception
        user.followers.add(self)

        # print message
        print(f"{self.username} started following {user.username}")

    def unfollow(self, user: "User") -> None:
        # TODO: only logged in users can unfollow
        if self in user.followers:
            user.followers.remove(self)
            # print message
            print(f"{self.username} unfollowed {user.username}")
        # TODO: check what to do if user is not in followers

    def publish_post(self, post_type: str, *args):
        # TODO: only logged in users can publish posts
        # TODO: check of better way to do this, abd how to print the message
        new_post = self.post_factory.create_post(post_type, self, *args)
        self.posts.append(new_post)
        return new_post

    def notify(self, message: str, log: bool, extra_message: str = ""):
        """
         Notify the user with the given message.
         If :log is True, the message will be printed to the console
        :param message: the message to notify the user with
        :param log: whether to print the message to the console
        :param extra_message: extra message to print
        :return: None
        """
        self.notifications.append(message)
        if log:
            print(f"notification to {self.username}: {message}{extra_message}")

    def print_notifications(self):
        print(f"{self.username}'s notifications:")
        for n in self.notifications:
            print(n)

    def __str__(self):
        return f'User name: {self.username}, Number of posts: {len(self.posts)}, Number of followers: {len(self.followers)}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, User):
            return self.username == other.username
        return False

    def __hash__(self):
        return hash(self.username)
