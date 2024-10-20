import unittest
from rental import Rental
from movie import Movie
from datetime import datetime


class RentalTest(unittest.TestCase):
    def setUp(self):
        self.new_movie = Movie(
            "Dune: Part Two", datetime.now().year, ["Sci-fi", "Action"]
        )
        self.regular_movie = Movie("Johnny English", 2003, ["Action", "Comedy"])
        self.childrens_movie = Movie("Frozen", 2013, ["Children", "Fairy Tale"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", 2000, ["Sci-fi", "Action"])
        self.assertEqual("Air", m.get_title())
        self.assertEqual(2000, m.year)
        self.assertTrue(m.is_genre("sci-fi"))

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.childrens_movie, 1)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.get_price(), 3)
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_price(), 2)
        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.get_price(), 3.5)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 1000)
        self.assertEqual(rental.get_rental_points(), 1000)
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 1000)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.childrens_movie, 1000)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.childrens_movie, 1)
        self.assertEqual(rental.get_rental_points(), 1)
