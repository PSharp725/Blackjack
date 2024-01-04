import random
import os
import sys

# Add the project's root directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_root)

from classes import card

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
                self.deck.append(card.Card(rank, suit))
    
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
    
    # outputs a new deck with the old deck appended. Needed for when you have less cards in the deck than need for a function (deal_hand)
    def new_deck(self):
        new_deck = Deck()
        new_deck.shuffle_deck()
        self.deck =  new_deck + self.deck
        
if __name__ == "__main__":
    
    # Keep This for now to know the code runs to completion
    new_card = card.Card()
    print(new_card.rank)
    print('This is the Last line')