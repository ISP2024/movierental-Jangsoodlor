from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""

    _instance = None

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance


class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_rental_points(self, days):
        """New release rentals earn 1 point for each day rented."""
        return days

    def get_price(self, days):
        """Straight $3 per day charge."""
        return 3 * days


class RegularPrice(PriceStrategy):
    """Pricing rules for Regular movies."""

    def get_rental_points(self, days):
        """Regular movie rentals earn 1 point."""
        return 1

    def get_price(self, days):
        """Two days for $2, additional days 1.50 per day."""
        return 2 + max(0, 1.5 * (days - 2))


class ChildrensPrice(PriceStrategy):
    """Pricing rules for Children movies."""

    def get_rental_points(self, days):
        """Children movie rentals earn 1 point."""
        return 1

    def get_price(self, days):
        """Three days for $1.50, additional days 1.50 per day."""
        return 1.5 + max(0, 1.5 * (days - 3))

NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDRENS = ChildrensPrice()
