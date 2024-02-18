from CostomExcption import InvalidCredentialsError
from posts.Post import Post


class SalePost(Post):
    def __init__(self, creator, product_name: str, price: float, city: str):
        super().__init__(creator)
        self.product_name = product_name
        self.price = price
        self.city = city
        self.isSold = False

    def discount(self, discount: float, password: str) -> None:
        """
        Reduces the price of the product by the given discount (in percentage) if the given password is correct.
        :param discount: discount percentage - a float in the range (0, 100]
        :param password: the password of the creator of the post
        :return: None
        """

        # TODO: what happen if the discount is not in the range (0, 100]?
        if discount <= 0 or discount > 100:
            raise ValueError("Discount must be in the range (0, 100]")

        if super().get_creator().password == password:
            self.price = self.price * (1 - discount / 100)
            print(f'Discount on {super().get_creator().username} product! the new price is: {self.price}')
        else:
            raise InvalidCredentialsError("Invalid credentials")

    def sold(self, password: str) -> None:
        """
        Marks the product as sold if the given password is correct.
        Print a message that the product is sold.
        :param password: the password of the creator of the post
        :return: None
        """
        if super().get_creator().password == password:
            self.isSold = True
            print(f'{super().get_creator().username}\'s product is sold')

    def __repr__(self):
        return f'{super().get_creator().username} posted a product for sale:\n{"Sold!" if self.isSold else "For sale!"} {self.product_name}, price: {self.price}, pickup from: {self.city}\n'
