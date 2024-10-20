import unittest
from datetime import datetime
from movie import Movie
from pricing import NEW_RELEASE, REGULAR, CHILDRENS


class PricingTest(unittest.TestCase):
    def setUp(self):
        """Create three movies: new release, children and regular movies."""
        self.new_release = Movie(
            "Bocchi the Rock", datetime.now().year, ["Anime", "Music"]
        )
        self.children_movie = Movie(
            "Tom and Jerry", datetime.now().year, ["Children", "Comedy"]
        )
        self.regular_movie = Movie("Johnny English", 2003, ["Action", "Comedy"])

    def test_get_children_movie(self):
        """Children movies should give Children price code"""
        self.assertEqual(self.children_movie.get_price_for_movie(), CHILDRENS)

    def test_get_regular_movie(self):
        """Regular movies should give Regular price code"""
        self.assertEqual(self.regular_movie.get_price_for_movie(), REGULAR)

    def test_get_new_release_movie(self):
        """New Release movies should give New Release price code"""
        self.assertEqual(self.new_release.get_price_for_movie(), NEW_RELEASE)
