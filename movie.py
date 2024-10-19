class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title):
        # Initialize a new movie.
        self.title = title

    def get_title(self):
        return self.title

    def get_price_code(self):
        # get the price code
        return self.price_code

    def __str__(self):
        return self.title
