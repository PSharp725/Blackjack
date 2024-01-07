import os
import sys

# Add the project's root directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_root)

from classes import card
from classes import deck
from classes import player
from classes import blackjack

class ClassTests:
    
    def __init__(self):
        pass

    def CardInitTest(self):
        # Testing the Card __init__ function 
        joker_card = card.Card()
        assert joker_card.rank== 'JOKER'
        assert joker_card.suit == 'JOKER'
        test_card = card.Card('ACE', 'SPADES')
        assert test_card.rank== 'ACE'
        assert test_card.suit == 'SPADES'
        
    def DeckInitTest(self):
        # Testing Deck __init__
        test_deck = deck.Deck()
        assert len(test_deck.deck) == test_deck.card_count 
        #test_deck.print_deck()
    
    def DeckShuffleTest(self):
        #Testing the Deck shuffle function
        test_deck = deck.Deck()
        test_deck.shuffle_deck()
        assert test_deck.deck != deck.Deck().deck
        #test_deck.print_deck()
        
    def CardPullTest(self):
        # Pull a card and test that the deck is down a card
        test_deck = deck.Deck()
        test_deck.shuffle_deck()
        test_pull = test_deck.pull_a_card()
        assert test_deck.card_count == len(test_deck.deck) and test_deck.card_count == 51
        #print(test_pull.rank + " of " + test_pull.suit )
        
if __name__ == "__main__":
    ClassTests.DeckInitTest()
    ClassTests.DeckShuffleTest()
    # Keep This for now to know the code runs to completion
    print('This is the Last line')