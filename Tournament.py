import secrets as scr
from Matchup import *
class Tournament():
    
    def __init__(self, tournament_title):
        self.__tournament_title   = tournament_title
        self.__tournamentUUID     = scr.token_hex(nbytes=16)
        self.__currRound          = 1
        self.__player_arr         = []
        self.__matchups           = []
        self.__currScoreBoard     = {}
    
    def showTournamentUUID(self):
        return self.__tournamentUUID
    
    def addPlayer(self, player):
        self.__player_arr.append(player)
        
    def showPlayers(self):
        for p in self.__player_arr:
            print("%s - %s" %(p.getPlayerName(), p.getPlayerDci()))
    
    def updateCurrScoreBoard(self):
        for p in self.__player_arr:
            self.__currScoreBoard[p.getPlayerName()] = p.getScore()

    def showCurrScoreBoard(self):
        for key,val in self.__currScoreBoard.items():
            print("Player: ", key,"| Score: ",val)

    def getLastMatcups(self):
        return self.__matchups

    def matchupExists(self,player_a,player_b):
        for match in self.__matchups:
            if player_a.getPlayerDci() == match.getPlayer(
                    'a').getPlayerDci() and player_b.getPlayerDci() == match.getPlayer('b').getPlayerDci():
                return True
            elif player_a.getPlayerDci() == match.getPlayer(
                    'b').getPlayerDci() and player_b.getPlayerDci() == match.getPlayer('a').getPlayerDci():
                return True
            else:
                return False

