



class Player:
    
    def __init__(self, player_type = "unassingned"):
        self.type = player_type
    
    def set_hand(self,hand = ['','']):
        self.hand = hand
    
    def get_hand(self):
        return self.hand