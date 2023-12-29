

from Blackjack.Classes import Card
from Blackjack.Classes import Deck
from Blackjack.Classes import Player




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
        for card in player.get_hand():
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