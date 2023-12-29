"""
   
This is an atempt at a Blackjack game
231220 - Present
Written By Patrick Sharp
   
"""


from Blackjack.Classes import Card
from Blackjack.Classes import Deck
from Blackjack.Classes import Player
from Blackjack.Classes import Blackjack


"""
import random

    
class Card:
    
    def __init__(self, rank = "JOKER", suit = "JOKER"):
        self.rank = rank
        self.suit = suit
    
    def get_rank_value(self):
        value_dic = {
            'ACE' : 11,
            'TWO' : 2,
            'THREE' : 3,
            'FOUR' : 4,
            'FIVE' : 5,
            'SIX' : 6,
            'SEVEN' : 7,
            'EIGHT' : 8,
            'NINE' : 9,
            'TEN' : 10,
            'JACK' : 10,
            'QUEEN' : 10,
            'KING' : 10
        }
        return value_dic.get(self.rank)
    
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
    

class Player:
    
    def __init__(self, player_type = "unassingned"):
        self.type = player_type
    
    def set_hand(self,hand = ['','']):
        self.hand = hand
    
    def get_hand(self):
        return self.hand
    
class Blackjack:
    
    def __init__(self):
        self.game_status = "Running"
    
    def deal_hand(self,deck):
        if len(deck) < 4:
            # WILL NEED TO HANDLE THIS EDGE CASE (SHUFFLE A NEW DECK TO DEAL THE EXTRA NEEDED CARDS MAYBE USE A WHILE LOOP TO CHECK INSTEAD OF A CONDITIONAL (CONTINUE KEYWORD))
            return
        players_hand = []
        dealers_hand = []
        for i in range(2):
            players_hand.append(deck.pull_a_card)
            dealers_hand.append(deck.pull_a_card)
        return (players_hand, dealers_hand)
    
    def check_blackjack(slef, player):
        blackjack_flag = False
        ace_flag = False
        sum = 0 
        # Check for 21
        for card in player.hand:
            if card.rank != "ACE" or player.type == "Dealer":
                sum += Card.get_rank_value(card)
                continue
            ace_flag = True
            sum += 1
        if sum == 21 or (ace_flag and sum + 10 == 21): blackjack_flag = True
        return blackjack_flag
    
    def hit_the_hand(self, player, deck):
        if len(deck) >= 1:
            # WILL NEED TO HANDLE THIS EDGE CASE
            pass
        player.hand.append(deck.pull_a_card)

    def hand_ace_flag(self,hand):
        for card in hand:
            if card.rank == "ACE": return True
        return False

    def hand_sum(self,player):
        sum = 0
        ace_flag = False
        if player.type != "Dealer":
            ace_flag = player.hand.hand_ace_flag(player.hand)
        for card in player.hand:
            if ~ace_flag: 
                sum += Card.get_rank_value(card)
                continue
            if card.rank != "ACE": 
                sum += Card.get_rank_value(card)
                continue
            sum += 1
        if ace_flag and sum + 10 <= 21:
            input (int("%d or %d"))(sum, sum+10)
"""


if __name__ == "__main__":
    
    # Testing the Card __init__ function 
    joker_card = Card()
    assert joker_card.rank== 'JOKER'
    assert joker_card.suit == 'JOKER'
    
    test_card = Card('ACE', 'SPADES')
    assert test_card.rank== 'ACE'
    assert test_card.suit == 'SPADES'
    
    
    
    # Testing Deck __init__
    test_deck = Deck()
    assert len(test_deck.deck) == test_deck.card_count
    #test_deck.print_deck()
    
    
    
    #Testing the Deck shuffle function
    test_deck.shuffle_deck()
    assert test_deck.deck != Deck().deck
    #test_deck.print_deck()
    
    
    
    # Pull a card and test that the deck is down a card
    test_pull = test_deck.pull_a_card()
    assert test_deck.card_count == len(test_deck.deck) and test_deck.card_count == 51
    #print(test_pull.rank + " of " + test_pull.suit )



    # Keep This for now to know the code runs to completion
    print('This is the Last line')