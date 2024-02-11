from posts.Post import Post
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


class ImagePost(Post):
    def __init__(self, creator, image_path: str):
        super().__init__(creator)
        self.image_url = image_path
        print(self)

    def display(self) -> None:
        # TODO: check if need to print message, or just display the image
        print("Shows picture")
        img = Image.open(self.image_url)
        # img_arr = np.array(img)
        # plt.imshow(img_arr)
        # plt.show()

    def __repr__(self):
        return f'{super().get_creator().username} posted a picture\n'
