class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title, price_code):
        # Initialize a new movie.
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_title(self):
        return self.title

    def get_rental_points(self, days):
        return self.price_code.get_rental_points(days)

    def get_price(self, days):
        return self.price_code.get_price(days)

    def __str__(self):
        return self.title
