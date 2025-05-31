# session 4

import random

class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, rank, suit):
        """
        Initialize a Card instance with validation
        :param rank: the card's rank (must be in RANKS)
        :param suit: the card's suit (must be in SUITS)
        """
        if rank not in self.RANKS:
            raise ValueError("invalid rank")
        if suit not in self.SUITS:
            raise ValueError("invalid suit")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """
        the card's rank
        :return: a string corresponding to the rank of the card
        """
        return self._rank

    @property
    def suit(self):
        """
        the card's suit
        :return: a string corresponding to the suit of the card
        """
        return self._suit

    def __str__(self):
        """
        Return human-readable string representation of card
        :return: card as rank+suit
        """
        return f"{self._rank}{self.suit}"

    def __repr__(self):
        """
        Return unambiguous string representation of card.
        :return: card as rank+suit
        """
        return self.__str__()  # repr is the same as str

    def __eq__(self, other):
        """
        Compare cards by rank only
        :param other: another Card instance to compare against
        :return: True if cards have same rank. False if they don't
        """
        return self.rank == other.rank

    def __lt__(self, other):
        """
        Compare cards by rank value
        :param other: another Card instance to compare against
        :return: True if self's rank is lower than other's. False otherwise
        """
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)


class Deck:
    def __init__(self):
        """
        Initialize a full deck of 52 cards in order
        """
        _cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                _cards.append(Card(rank, suit))
        self._cards = _cards  # this is a data structure, it is a list

    @property
    def cards(self):
        """
        The list of cards in the deck
        :return: list of the card objects that make up the deck
        """
        return self._cards

    def __str__(self):
        """
        Return string representation of the entire deck
        :return: All cards in deck as string
        """
        return str(self._cards)
    # string is used when printing individual cards

    def shuffle(self):
        """
        Randomly shuffle the deck in place
        :return: A string with the cards of the deck in a random order
        """
        random.shuffle(self.cards)

    def deal(self):
        """
        Remove and return the top card from the deck, simulating a deal
        :return: the dealt card
        """
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
