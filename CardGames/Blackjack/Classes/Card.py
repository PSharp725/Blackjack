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
    
if __name__ == "__main__":
    
    # Keep This for now to know the code runs to completion
    print('This is the Last line')