from collections.abc import Collection
from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title: str, year: int, genre: Collection[str]):
        # Initialize a new movie.
        self.title = title
        self.year = year
        self.genre = genre

    def get_title(self) -> str:
        return self.title

    def is_genre(self, genre: str):
        return genre.lower() == self.genre.lower()

    def __str__(self) -> str:
        return f"{self.title} {self.year}"
