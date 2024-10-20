import re
import unittest
from customer import Customer
from datetime import datetime
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase):
    """Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie(
            "Dune: Part Two", datetime.now().year, ["Sci-fi", "Action"]
        )
        self.regular_movie = Movie("Johnny English", 2003, ["Action", "Comedy"])
        self.childrens_movie = Movie("Frozen", 2013, ["Children", "Fairy Tale"])

    def test_billing(self):
        self.c.add_rental(Rental(self.new_movie, 5))
        self.assertEqual(self.c.get_total_charge(), 15)
        self.c.add_rental(Rental(self.childrens_movie, 5))
        self.assertEqual(self.c.get_total_charge(), 15+4.5)
        self.c.add_rental(Rental(self.regular_movie, 5))
        self.assertEqual(self.c.get_total_charge(), 15+4.5+6.5)

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace("\n", ""), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])

    def test_get_total_rental_points(self):
        self.c.add_rental(Rental(self.new_movie, 5))
        self.assertEqual(self.c.get_total_rental_points(), 5)
        self.c.add_rental(Rental(self.regular_movie, 5))
        self.assertEqual(self.c.get_total_rental_points(), 6)
        self.c.add_rental(Rental(self.childrens_movie, 5))
        self.assertEqual(self.c.get_total_rental_points(), 7)
