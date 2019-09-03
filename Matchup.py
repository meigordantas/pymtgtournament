from Player import *


class Matchup():

    def __init__(self, player_a, player_b, round):
        self.__matchRound = round
        self.__isFinnished = False
        self.__player_a = player_a
        self.__player_b = player_b
        self.__matchWinner = None

    def getWinner(self):
        return self.__matchWinner

    def setWinner(self, resultParam):
        if resultParam in [0, 1, 2]:
            if resultParam == 0:
                self.__isFinnished = True
            elif resultParam == 1:
                self.__isFinnished = True
                self.__matchWinner = self.__player_a
            else:
                self.__matchWinner = self.__player_b
        else:
            raise ValueError('resultParam must be 0, 1 or 2')

    def getPlayers(self):
        print("%s vs %s" % (self.__player_a.getPlayerName(), self.__player_b.getPlayerName()))



