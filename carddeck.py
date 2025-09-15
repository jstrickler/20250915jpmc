import random
from card import Card
# from card2 import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return f"{type(self).__name__}:{len(self._cards)}"
    
    def __add__(self, other):  # implement '+'
        class_of_self = type(self)
        d = class_of_self()

      #  d = type(self)()
        d._cards = self._cards + other._cards
        return d

    def __repr__(self):
        type_of_self = type(self)
        name_of_self = type_of_self.__name__
        return f"{type(self).__name__}()"

    @classmethod
    def get_suits(cls):
        return cls.SUITS

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    print(f"{d1 = }")
    d1.shuffle()
    print(f"{d1.cards = }")
    for _ in range(5):
        card = d1.draw()
        print(f"{card = }")
    print(d1)
    print(len(d1))
    d3 = d1 + d2  # calls d1.__add__()...
    print(d3)
    print(d1.get_suits())
    print(CardDeck.get_suits())