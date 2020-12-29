import random

suits = ['Hearts','Diamonds','Spades','Clubs']
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        # card passed in 
        # from Deck.deal() --> single Card(suit,rank)
        self.cards.append(card)
        self.values = values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        
        # if total value > 21 and I still have an ace
        # then change my ace to be a 1 instead of an 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1