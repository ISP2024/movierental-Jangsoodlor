import logging
from collections.abc import Collection
from typing import Optional
from dataclasses import dataclass


class MovieCatalog:
    """A catalog of available movies."""

    _instance = None

    def __init__(self):
        """Initialize a new movie catalog."""
        self.catalog = []
        self.logger = logging.getLogger(__name__)
        self.movie_gen_iter = iter(self.movie_generator())

    def movie_generator(self):
        for line_num, row in enumerate(open("movies.csv", "r")):
            yield line_num+1, row.strip()

    def create_movie(self, line_num, row):
        """Create a single movie from a row in movies.csv."""
        movie_info = row.split(",")
        try:
            if movie_info[0][0] != "#":
                title = movie_info[1]
                year = int(movie_info[2])
                genre = movie_info[3].split("|")
                movie = Movie(title=title, year=year, genre=genre)
                self.catalog.append(movie)
                return movie
        except (IndexError, ValueError):
            self.logger.error(f"Line {line_num}: Unrecognized format \"{row}\"")
            return None

    def is_valid_movie(self, movie, title: str, year: Optional[int]):
        """Return True if the movie has the same title and year as the parameters."""
        if movie is not None:
            if not year:
                return movie.title == title
            return movie.title == title and movie.year == year
        return False

    def get_movie(self, title: str, year: Optional[int] = None):
        """Return a movie with matching title and optional year."""
        movies = [movie for movie in self.catalog if movie.title == title]
        if year is not None:
            movies = [movie for movie in movies if movie.year == year]
        if len(movies) == 0:
            try:
                while True:
                    row = next(self.movie_gen_iter)
                    movie = self.create_movie(row[0], row[1])
                    if self.is_valid_movie(movie, title, year):
                        return movie
            except StopIteration:
                return None
        return movies[0]

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
        return cls._instance


@dataclass(frozen=True)
class Movie:
    """A movie available for rent."""

    title: str
    year: int
    genre: Collection[str]

    def get_title(self) -> str:
        return self.title

    def is_genre(self, genre: str):
        return genre.lower() == self.genre.lower()

    def __str__(self) -> str:
        return f"{self.title} {self.year}"
