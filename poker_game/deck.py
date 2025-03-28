# session 4

import random


class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError("invalid rank")
        if suit not in self.SUITS:
            raise ValueError("invalid suit")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return f"{self._rank}{self.suit}"

    def __repr__(self):
        return self.__str__()  # repr is the same as str

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)

class Deck:
    def __init__(self):
        _cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                _cards.append(Card(rank, suit))
        self._cards = _cards  # this is a data structure, it is a list

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self._cards)
    # string is used when printing individual cards

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)


if __name__ == "__main__":
    c1 = Card("A", "♣")
    print(c1.suit, c1.rank)

    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
    print(deck)
