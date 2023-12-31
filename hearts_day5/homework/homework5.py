# перепишіть клас Card (fifth_day.practice.05_hearts.Card) доповнивши методи
# порівнянь __eq__ і __lt__ первіркою типу аргумента oter і відповідним виключенням
# у випадку невідповідності очікуванням. Визначтесь - який це повинен бути exception
# (ValueError, NotImplementedError, TypeError або інший). Поясніть в коментах.
# Завдання з зірочкою) Додайте можливість виводити значення карт в консоль не в
# простому чорно-білому зображенні, а в кольоровому. Можливо - додайте кольори фону
# і стиль. Поексперементуйте і запропонуйте найбілш виразний на Ваш погляд варіант.
# Поясніть в коментарі вибір бібліотеки
# Рекомендовані для використання бібліотеки і матеріали:
# https://pypi.org/project/colorama/
# https://pypi.org/project/termcolor/
# https://www.askpython.com/python/examples/print-colored-text-to-the-terminal-in-python
# https://www.geeksforgeeks.org/print-colors-python-terminal/

class Card:
    SUITS = "♠ ♣ ♥ ♦".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, suit: str, rank:str) ->None:
        if suit not in self.SUITS:
            raise ValueError(f"value of suits must be from {self.SUITS}, but got {suit}")
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.suit}{self.rank}"

    @property
    def value(self) -> int:
        return self.RANKS.index(self.rank)

    @property
    def points(self) -> int:
        if self.suit == "♠ " and self.rank == "Q":
            return 13
        if self.suit == "♥":
            return 1
        return 0

    def __eq__(self, other: "Card") -> bool:
        if not isinstance(other, Card):
            raise TypeError(f"unsupported operand type(s) for ==: 'Card' and '{type(other)}'")
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other: "Card") -> bool:
        return self.value < other.value
