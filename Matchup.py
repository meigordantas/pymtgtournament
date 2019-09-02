from Player import *

class Matchup():

    def __init__(self, player_a, player_b, round):
        self.__matchRound = round
        self.__player_a = player_a
        self.__player_b = player_b
        self.__matchWinner = None

    def getWinner(self):
        return self.__matchWinner 
    
    def setMatchRsult(self, result, player):
        if result in (0,1):
            return None
        else:
            if player in ('a','A','1'):
                self.__matchWinner = self.__player_a
            elif player in ('b','B','2'):
                self.__matchWinner = self.__player_b

    def getPlayers(self, player):
        print("%s vs %s" %(self.__player_a.getPlayerName(), self.__player_b.getPlayerName()))
    

    
