import random
from typing import Tuple, List, Sequence, TypeVar, Optional


SUITS = "♠ ♣ ♥ ♦".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

Card = Tuple[str, str] # tuple[str,str]
Deck = List[Card] # list[Card]

Choosable = TypeVar("Choosable")

def get_deck(shuffle: bool = False)-> Deck:
    """Get a new deck of 52 cards"""
    deck = [(s,r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

def choose(items: Sequence[Choosable]) -> Choosable:
    return  random.choice(items)

def player_order(names: List[str], start: Optional[str] = None) -> List[str]:
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]

def deal_hands(deck):
    """Deal the cards in the deck into four hands"""
    return deck[0::4], deck[1::4], deck[2::4], deck[3::4]

def play() -> None:
    """Play a 4-player card game"""
    deck = get_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names,deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start = start_player)

    while hands[start_player]:
        for name in turn_order:
            card = choose(hands[name])
            hands[name].remove(card)
            print(f"{name}: {card[0] + card[1]:<3}", end ="")
        print()

if __name__ == '__main__':
    play()