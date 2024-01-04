from classes import card
from classes import deck
from classes import player
from classes import blackjack

class ClassTests:

    def CardInitTest():
        # Testing the Card __init__ function 
        joker_card = card.Card()
        assert joker_card.rank== 'JOKER'
        assert joker_card.suit == 'JOKER'
        test_card = card.Card('ACE', 'SPADES')
        assert test_card.rank== 'ACE'
        assert test_card.suit == 'SPADES'
        
    def DeckInitTest():
        # Testing Deck __init__
        test_deck = deck.Deck()
        assert len(test_deck.deck) == test_deck.card_count 
        #test_deck.print_deck()
    
    def DeckShuffleTest():
        #Testing the Deck shuffle function
        test_deck = deck.Deck()
        test_deck.shuffle_deck()
        assert test_deck.deck != deck.Deck().deck
        #test_deck.print_deck()
        
    def CardPullTest():
        # Pull a card and test that the deck is down a card
        test_deck = deck.Deck()
        test_deck.shuffle_deck()
        test_pull = test_deck.pull_a_card()
        assert test_deck.card_count == len(test_deck.deck) and test_deck.card_count == 51
        #print(test_pull.rank + " of " + test_pull.suit )
        
if __name__ == "__main__":
    
    # Keep This for now to know the code runs to completion
    print('This is the Last line')