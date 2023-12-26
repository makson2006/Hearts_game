from typing import Optional


class Genre:

    def __init__(self, name: str, description: Optional[str] = None)->None:
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return self.name

    def __repr__(self) ->str:
        return f"Genre({self.name}, {self.description}"

class Author:
    def __init__(self,first_name: str, last_name: str, year_of_birth: Optional[int] = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        return f"Author({self.first_name}, {self.last_name}, {self.year_of_birth}"

    def __eq__(self, other: "Author")-> bool:
        if not isinstance(other, Author):
            raise TypeError(f"for type Author and type {type(other)} operation is not implemented")
        return self.first_name == other.first_name and self.last_name == other.last_name and self.year_of_birth == other.year_of_birth

    def __hash__(self):
        return  hash((self.first_name, self.last_name, self.year_of_birth))

class Book:
    def __init__(self, name: str, language: str, authors: list[Author], genres: list[Genre], year: int, isbn: str, describe: Optional[str] = None):
        self.name = name
        self.language = language
        self.authors = authors
        self.genres = genres
        self.year = year
        self.year = year
        self.isbn = isbn
        self.describe = describe


    def __eq__(self, other: "Book") -> bool:
        return set(self.authors) == set(other.authors) and self.name == other.name

