import os
import sys

# Add the project's root directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_root)

from classes import card
from classes import deck
from classes import player

class Blackjack:
    
    def __init__(self):
        self.game_status = "Running"
        self.game_deck = deck.Deck()
        self.game_deck = self.game_deck.shuffle_deck()
    
    def deal_hand(self):
        if len(self.game_deck) < 4:
            self.game_deck.new_deck()
        players_hand = []
        dealers_hand = []
        for i in range(2):
            players_hand.append(self.game_deck.pull_a_card)
            dealers_hand.append(self.game_deck.pull_a_card)
        return (players_hand, dealers_hand)
    
    def check_blackjack(slef, player):
        blackjack_flag = False
        ace_flag = False
        sum = 0 
        # Check for 21
        for card in player.get_hand():
            if card.rank != "ACE" or player.type == "Dealer":
                sum += card.get_rank_value(card)
                continue
            ace_flag = True
            sum += 1
        if sum == 21 or (ace_flag and sum + 10 == 21): blackjack_flag = True
        return blackjack_flag
    
    def hit_the_hand(self, player):
        if len(self.game_deck) >= 1:
            self.game_deck.new_deck()
        player.hand.append(self.game_deck.pull_a_card())

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
                sum += card.get_rank_value(card)
                continue
            if card.rank != "ACE": 
                sum += card.get_rank_value(card)
                continue
            sum += 1
        if ace_flag and sum + 10 <= 21:
            temp = input (int("%d or %d"))(sum, sum+10)
            
    def play_game(self):
        curr_game = Blackjack()
        dealer = player.Player('Dealer')
            
            
if __name__ == "__main__":
    
    # Keep This for now to know the code runs to completion
    print('This is the Last line')