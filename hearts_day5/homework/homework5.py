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

import sys
import random
from colorama import Fore, Back, Style, init

init(autoreset=True)

class Card:
    SUIT_COLORS = {"♠": Fore.BLACK, "♣": Fore.BLACK, "♥": Fore.RED, "♦": Fore.RED}
    SUITS = list(SUIT_COLORS.keys())
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, suit: str, rank: str) -> None:
        if suit not in self.SUITS:
            raise ValueError(f"value of suits must be from {self.SUITS}, but got {suit}")
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        color = self.SUIT_COLORS.get(self.suit, Fore.WHITE)
        return f"{color}{self.suit}{self.rank}"

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

class Deck:
    def __init__(self,cards):
        self.cards = cards

    @classmethod
    def create(cls, shuffle = False):
        """Create a new deck of 52 cards"""
        cards = [Card(s,r) for r in Card.RANKS for s in Card.SUITS]
        if shuffle:
            random.shuffle(cards)
        return cls(cards)

    def deal(self, num_hands: int):
        cls = self.__class__
        return tuple(cls(self.cards[i::num_hands]) for i in range(num_hands))


class Player:
    def __init__(self, name: str, hand: Deck) -> None:
        self.name = name
        self.hand = hand

    def play_card(self) -> Card:
        """Play a card from the player's hand."""
        card = random.choice(self.hand.cards)
        self.hand.cards.remove(card)
        print(f" {self.name}:{card!r:<3}", end="")


class Game:
    def __init__(self, *names: str) -> None:
        deck = Deck.create(shuffle = True)
        self.names = (list(names) + "P1 P2 P3 P4".split())[:4] if names else "P1 P2 P3 P4".split()[:4]
        self.hands = {
            n: Player(n,h) for n, h in zip(self.names, deck.deal(4))
        }

    def player_order(self,start=None):
        if start is None:
            start = random.choice(self.names)
        start_idx = self.names.index(start)
        return self.names[start_idx:] + self.names[:start_idx]
    def play(self) ->None:
        """Play a card game"""
        start_player = random.choice(self.names)
        turn_order = self.player_order(start=start_player)

        while self.hands[start_player].hand.cards:
            for name in turn_order:
                self.hands[name].play_card()
            print()

if __name__ == '__main__':
    player_names = sys.argv[1:]
    game = Game(*player_names)
    game.play()


