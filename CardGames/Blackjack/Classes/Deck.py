

import random
from Blackjack.Classes import Card




class Deck:
    
    def __init__(self):
        self.card_count = 52
        
        Ranks = [
            'ACE',
            'TWO',
            'THREE',
            'FOUR',
            'FIVE',
            'SIX',
            'SEVEN',
            'EIGHT',
            'NINE',
            'TEN',
            'JACK',
            'QUEEN',
            'KING']
        
        Suits = [
            'SPADES',
            'HEARTS',
            'DIAMONDS',
            'CLUBS']
        
        self.deck = []
        for suit in Suits:
            for rank in Ranks:
                self.deck.append(Card(rank, suit))
    
    def shuffle_deck(self):
        random.shuffle(self.deck)
        
    def print_deck(self):
        print('\n Start of The deck \n')
        for i in range (52):
            print(self.deck[i].rank, self.deck[i].suit)
        print('\n End of the deck \n')
    
    def pull_a_card(self):
        pulled_card = self.deck[-1]
        self.deck.pop()
        self.card_count -= 1
        return pulled_card