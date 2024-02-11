from posts.Post import Post
from posts.ImagePost import ImagePost
from posts.SalePost import SalePost
from posts.TextPost import TextPost


class PostFactory:
    @staticmethod
    def create_post(post_type: str, creator, *args) -> Post:
        if post_type == "Text":
            return TextPost(creator, *args)
        if post_type == "Image":
            return ImagePost(creator, *args)
        if post_type == "Sale":
            return SalePost(creator, *args)
        raise ValueError("Invalid post type")
