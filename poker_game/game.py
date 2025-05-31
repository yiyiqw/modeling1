# session 4 + 5 continued
from deck import Deck, Card  # shuffles the deck


class Hand:
    """
    A class representing a 5-card poker hand with evaluation methods
    """
    def __init__(self, deck):
        """
        Initialize a hand by dealing 5 cards from a deck
        :param deck: the deck to deal cards from
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        The cards in the hand
        :return: list of five cards (the hand)
        """
        return self._cards

    def __str__(self):
        """
        Return string representation of the hand.
        :return: string with all cards in hand
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Check if all cards are of the same suit (condition for a flush)
        :return: True if hand is a flush. False otherwise
        """
        for card in self.cards[1:]:  # looking from the second card onwards
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def num_matches(self):
        """
        Count rank matches between cards (which is a pair of cards with the same rank)
        :return: total number of matching rank pairs
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Check if hand contains exactly one pair
        :return: True if hand has exactly one pair. False otherwise
        """
        if self.num_matches == 2:
            return True
        return False

    @property
    def is_2_pair(self):
        """
        Check if hand contains exactly two pairs
        :return: True if hand has exactly two pairs. False otherwise
        """
        if self.num_matches == 4:
            return True
        return False

    @property
    def is_trips(self):
        """
        Check if hand contains three of a kind
        :return: True if hand has three of a kind. False otherwise
        """
        if self.num_matches == 6:
            return True
        return False

    @property
    def is_quade(self):
        """
        Check if hand contains four of a kind.
        :return: True if hand has four of a kind. False otherwise
        """
        if self.num_matches == 12:
            return True
        return False

    @property
    def is_full_house(self):
        """
        Check if hand contains a full house (three  with same rank + pair)
        :return: True if hand is a full house. False otherwise
        """
        if self.num_matches == 8:
            return True
        else:
            return False

    @property
    def is_straight(self):
        """
        Check if hand contains five sequential ranks and not repeated (condition for a straight)
        :return:  True if hand is a straight. False otherwise
        """
        if self.num_matches != 0:
            return False
        self.cards.sort()
        if Card.RANKS.index(self.cards[-1].rank) != Card.RANKS.index(self.cards[0].rank) + 4:
            return False
        return True


matches = 0
count = 0
while matches < 100:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    count += 1
    if hand.is_straight:
        # print(hand)
        matches += 1
        # break


print(f"The probability of straight is {100 * matches / count}%")
