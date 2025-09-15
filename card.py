class Card: # inherits from class 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):  # getter property
        return self._rank

    @rank.setter
    def rank(self, new_value):  # setter property
        if isinstance(new_value, str):
            self._rank = new_value
        else:
            raise TypeError("rank must be a str")

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        self._suit = value

    def __str__(self):
        return f"Card:{self.rank}/{self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card("8", "Diamonds")
    c2 = Card("A", "Hearts")
    print(c1)  # str
    print(f"{c1 = }")  # repr
    print(f"{c1.rank = }")
    print(f"{c1.suit = }")
    c1.rank = '9'
    print(f"{c1.rank = }")
