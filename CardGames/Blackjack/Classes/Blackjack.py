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
        #Blackjack.deal_hand(self)
        
    def deal_hand(self,game_deck: deck, dealer: player, human: player, bet: int):
        self.bet = bet
        if game_deck.card_count  <= 4:
            game_deck.new_deck()
        for i in range(2): 
            human.hand.append(game_deck.pull_a_card()) 
            dealer.hand.append(game_deck.pull_a_card()) 
    
    def check_blackjack(self,player: player):
        blackjack_flag = False
        ace_flag = False
        sum = 0 
        # Check for 21
        for card in player.get_hand():
            if card.rank != "ACE" or player.type == "Dealer":
                sum += card.get_rank_value()
                continue
            ace_flag = True
            sum += 1
        if sum == 21 or (ace_flag and sum + 10 == 21): blackjack_flag = True
        return blackjack_flag
    
    def hit_the_hand(self, game_deck: deck, player: player):
        if game_deck.card_count <= 1:
            game_deck.new_deck()
        player.hand.append(game_deck.pull_a_card())

    def hand_ace_flag(self,hand):
        for card in hand:
            if card.rank == "ACE": return True
        return False

    def hand_sum(self,player):
        sum = 0
        ace_flag = False
        if player.type != "Dealer":
            ace_flag = self.hand_ace_flag(player.hand)
        for card in player.hand:
            if ~ace_flag or card.rank != "ACE": 
                sum += card.get_rank_value()
                continue
            sum += 1
        if ace_flag and sum + 10 <= 21:
            temp = input (int("%d or %d"))(sum, sum+10)
            sum = temp
        return sum
        
    def game_outcome(self):
        if self.game_status == "Draw": return 0
        elif self.game_status == "Win": return self.bet * 2
        elif self.game_status == "Lose": return -self.bet
               
    def play_game(self):
        curr_game = Blackjack()
        game_deck = deck.Deck()
        game_deck.build_deck()
        game_deck.shuffle_deck()
        dealer = player.Player('Dealer')
        human_player = player.Player('Human')
        player_money_total = 10_000.00
        while True:
            while curr_game.game_status == "Running":
                    bet = int(input(f"How much do you want to bet? You have ${player_money_total:.2f}\n"))
                    curr_game.deal_hand(game_deck, dealer, human_player,bet)
                    dealer_blackjack = curr_game.check_blackjack(dealer)
                    human_blackjack = curr_game.check_blackjack(human_player) 
                    if dealer_blackjack and human_blackjack:
                        curr_game.game_status = "Draw"
                        continue
                    elif human_blackjack:
                        curr_game.game_status = "Win"
                        continue
                    elif dealer_blackjack:
                        curr_game.game_status = "Lose"
                        continue
                    human_players_turn = True
                    while human_players_turn:
                        human_hand_sum = curr_game.hand_sum(human_player)
                        print(f"You have a {human_hand_sum}")
                        human_move = int(input("What do you want to do?\n \
                                                1.) Hit\n \
                                                2). Stand\n"))
                        if human_move == 1:
                            curr_game.hit_the_hand(game_deck, human_player)
                            human_hand_sum = curr_game.hand_sum(human_player)
                            if human_hand_sum > 21 : 
                                curr_game.game_status = "Lose"
                                print(f"{human_hand_sum} Bust")
                                break
                            elif human_hand_sum == 21 :
                                print("21")
                                break
                        elif human_move == 2: break
                    dealer_sum = curr_game.hand_sum(dealer)
                    while dealer_sum < 17:
                        curr_game.hit_the_hand(game_deck, dealer)
                        dealer_sum = curr_game.hand_sum(dealer)
                    dealer_sum = curr_game.hand_sum(dealer)
                    print (f'The dealer has {dealer_sum}')
                    if curr_game.game_status == "Lose": pass
                    elif dealer_sum > human_hand_sum and human_hand_sum <= 21:
                        curr_game.game_status = "Lose"
                    elif human_hand_sum > dealer_sum and human_hand_sum <= 21:
                        curr_game.game_status = "Win"
                    elif human_hand_sum == dealer_sum and human_hand_sum <= 21:
                        curr_game.game_status = "Draw"
                    else: curr_game.game_status = "Error"
                    money_outcome = curr_game.game_outcome()
                    player_money_total += money_outcome
                    print(f'You {curr_game.game_status}')
                    break
            break
                        
                        
                
if __name__ == "__main__":
    
    # Keep This for now to know the code runs to completion
    print('This is the Last line of ' + __file__)