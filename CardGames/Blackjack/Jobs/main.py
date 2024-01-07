"""
   
This is an atempt at a Blackjack game
231220 - Present
Written By Patrick Sharp
   
"""

import os
import sys

# Add the project's root directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_root)

# Now you can perform relative imports
from classes import card
from classes import deck
from classes import player
from classes import blackjack


def main():
    pass


if __name__ == "__main__":
    
    # Keep This for now to know the code runs to completion
    test_crad = card.Card()
    test_deck = deck.Deck()
    test_player = player.Player()
    test_game = blackjack.Blackjack()
    test_game.play_game()
    #print(sys.path)
    print('This is the Last line of ' + __file__)