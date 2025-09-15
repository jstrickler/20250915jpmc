from card import Card
from carddeck import CardDeck

class Game:
    def play(self):
        print("Playing...")

class JokerDeck(Game, CardDeck):
    def _make_deck(self):
        super()._make_deck()  # super()
        for joker_number in 1, 2:
            joker = Card(f"JOKER-{joker_number}", "*** JOKER ***")
            self._cards.append(joker)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(j.cards)
    print(j)
    print(f"{JokerDeck.mro() = }")
    j.play()