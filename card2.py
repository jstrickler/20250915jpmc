from dataclasses import dataclass

@dataclass
class Card:
    rank: str
    suit: str

if __name__ == "__main__":
    c1 = Card('8', 'Diamonds')
    print(c1)
    print(f"{c1 = }")
