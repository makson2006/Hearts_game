# Модифікувати клас книги з ДЗ 3 таким чином, щоб параметри які ми передаємо при ініціалізації екземпляру були:
# - name, language, year - обовʼязковими
# - автори - передавались не списком а як звичайні позиційні аргументи
# - опис книги, isbn, genres - необовʼяккові параметри і лише як ключові
# (підказки тут https://docs.python.org/3/tutorial/controlflow.html#special-parameters)
#
#
# - створіть метод у книги який повертає вік книги в роках (відносно поточного)
# (підказки тут - https://docs.python.org/3/library/datetime.html)

from typing import Optional
from datetime import date

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
    # ДЗ змінити параметри
    def __init__(self, name: str, language: str, year: int, authors: Author, *, describe: Optional[str] = None, isbn: Optional[str] = None, genres: Optional[list[Genre]] = None):
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

    def get_age(self):
        today = date.today()
        return today.year - self.year

book = Book(
    name="Гордість і упередження",
    language="англійська",
    year=2020,
    authors=Author("Джейн", "Ostin"),
    describe="Класичний роман про манери, який досліджує любов, шлюб і соціальний клас.",
    isbn="978-1234567890",
    genres=[Genre("Роман", "Історичний роман")]
)
print(book.get_age())
# print(book.name,'\n',book.authors,'\n',book.language,'\n',book.year)
