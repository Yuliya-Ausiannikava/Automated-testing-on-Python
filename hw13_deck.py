"""
A program that contains a list of cards, can shuffle them,
and allows the user to select a card from the deck by its number.
"""

import random


class Card:

    number_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    mast_list = ['♠', '♥', '♦', '♣']
    jokers_list = ['Red Joker', 'Black Joker']

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast

    def __str__(self):
        return f"{self.number} {self.mast}"


class CardsDeck:
    def __init__(self):
        self.cards = []
        for mast in Card.mast_list:
            for number in Card.number_list:
                self.cards.append(Card(number, mast))
        for joker in Card.jokers_list:
            self.cards.append(Card(joker, ''))

    def shuffle(self):
        random.shuffle(self.cards)

    def get_cards(self, index):
        if 0 <= index < len(self.cards):
            return self.cards[index]
        else:
            raise IndexError("You must enter an index from 0 to 53")


deck = CardsDeck()
deck.shuffle()
card_number = int(input('Choose a card from a deck of 54 cards: '))
card = deck.get_cards(card_number)
print(f'You card is: {card}')

card_number = int(input('Choose a card from a deck of 54 cards: '))
card = deck.get_cards(card_number)
print(f'You card is: {card}')
