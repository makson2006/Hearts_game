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


