from posts.Post import Post


class TextPost(Post):
    def __init__(self, creator, content: str):
        super().__init__(creator)
        self.content = content
        print(self)

    def __repr__(self):
        return f'{super().get_creator().username} published a post:\n"{self.content}"\n'
