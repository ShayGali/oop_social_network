import matplotlib.pyplot as plt
from PIL import Image

from posts.Post import Post


class ImagePost(Post):
    def __init__(self, creator, image_path: str):
        super().__init__(creator)
        self.image_url = image_path
        print(self)

    def display(self) -> None:
        print("Shows picture")
        img = Image.open(self.image_url)
        plt.imshow(img)
        plt.show()

    def __repr__(self):
        return f'{super().get_creator().username} posted a picture\n'
