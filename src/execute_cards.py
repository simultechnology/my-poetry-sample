from random import choice
from playing_cards.french_deck import Card, FrenchDeck


def main():
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck))

    print(deck[0])
    print(deck[-1])

    print(choice(deck))
    print(choice(deck))
    print(choice(deck))

    print(deck[:3])
    print(deck[12::13])

    print('---enumerate---')
    for i, card in enumerate(deck):
        i = i + 1
        if i % 13 == 0:
            end = '\n'
        else:
            end = ', '
        print(card, end=end)

    print('---reversed---')
    for card in reversed(deck):
        print(card, end=', ')
    print()

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    print('---2 enumerate---')
    for i, card in enumerate(sorted(deck, key=spades_high)):
        i = i + 1
        if i % 13 == 0:
            end = '\n'
        else:
            end = ', '
        print(card, end=end)


main()
