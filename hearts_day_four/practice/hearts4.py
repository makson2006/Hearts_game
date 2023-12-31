
import random
import sys


class Card:
    SUITS = "♠ ♣ ♥ ♦".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, suit: str, rank:str) ->None:
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.suit}{self.rank}"

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
        print(f"{self.name}: {card!r:<3}", end="")


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


