# Card.py
"""Class for playing cards"""
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 12 Feb 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Example: Card Class
#     Source: Python Programming
#    Chapter: 10
#
# Program Description
#   Implementation of a class for a playing card
#
# Algorithm (pseudocode)
#   
#   
#   
#   
#   

from random import randrange


class Card:
    def __init__(self, suit, rank):
        """
        Card constructor method
        :param suit: int -> 0 = hearts, 1 = diamonds, 2 = clubs, 3 = spades
        :param rank: int -> number rank of card
        """
        self.suit = suit
        self.rank = rank
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['null', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def setSuit(self, arg):
        """Sets the suit (int, 0-4) of an individual card"""
        self.suit = arg

    def setRank(self, arg):
        self.rank = arg

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def getSuitName(self):
        return self.suits[self.suit]

    def getRankName(self):
        return self.ranks[self.rank]

    def toString(self):
        print('Suit: {} ({})\tRank: {} ({})'.format(self.getSuitName(), self.getSuit(), self.getRankName(), self.getRank()))


class Deck:
    def __init__(self):
        self.cards = []

        for s in range(4):
            for r in range(1, 14):
                self.cards.append(Card(s, r))

    def getDeck(self):
        return self.cards

    def shuffle(self):
        for i in range(self.getLength()):
            card1 = randrange(self.getLength()); card2 = card1
            while card2 == card1:
                card2 = randrange(self.getLength())
            self.swap(card1, card2)

    def swap(self, card1, card2):
        self.cards[card1], self.cards[card2] = self.cards[card2], self.cards[card1]

    def cut(self):
#        length // 2 - length // 10
        cutPoint = 26
        cut1 = self.cards[:26]
        cut2 = self.cards[27:]
        self.cards = cut2 + cut1

    def getLength(self):
        return len(self.cards)

    def toString(self):
        for card in self.cards:
            card.toString()


def main():
    deck = Deck()
    deck.cut()
    deck.toString()

if __name__ == '__main__':
    main()
