from typing import Set, List

from PostFactory import PostFactory


class User:
    def __init__(self, username: str, password: str):
        if len(password) < 4 or len(password) > 8:
            raise ValueError("Password must be 4 to 8 characters long")

        self.username = username
        self.password = password

        self.followers: Set["User"] = set()
        self.num_of_posts = 0
        self.notifications: List[str] = []
        self.post_factory = PostFactory()

    def follow(self, user: "User") -> None:
        """
        Follow the given user.
        The given user followers set will be updated accordingly.
        Args:
            user: the user to follow

        Returns:
            None
        """
        # TODO: only logged in users can follow
        if user == self:
            raise ValueError("Cannot follow yourself")  # TODO: check if need to raise an exception
        user.followers.add(self)

        # print message
        print(f"{self.username} started following {user.username}")

    def unfollow(self, user: "User") -> None:
        """
        Unfollow the given user.
        The given user followers set will be updated accordingly.
        """
        # TODO: only logged in users can unfollow
        if self in user.followers:
            user.followers.remove(self)
            # print message
            print(f"{self.username} unfollowed {user.username}")
        # TODO: check what to do if user is not in followers

    def publish_post(self, post_type: str, *args):
        """
        Publish a post of the given type.
        The post will be created using the post factory.
        Args:
            post_type: the type of the post to create.
            Will be in ["Text", "Image", "Sale"]
            *args: the arguments to pass to the post.
            See the `PostFactory.py` for more details
        """
        # TODO: only logged in users can publish posts
        new_post = self.post_factory.create_post(post_type, self, *args)
        self.num_of_posts += 1
        return new_post

    def notify(self, message: str, log: bool, extra_message: str = ""):
        """
         Notify the user with the given message.
         If the log is True, the message will be printed to the console
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
        return f'User name: {self.username}, Number of posts: {self.num_of_posts}, Number of followers: {len(self.followers)}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, User):
            return self.username == other.username
        return False

    def __hash__(self):
        return hash(self.username)
