import secrets as scr
class Tournament():
    
    def __init__(self, tournament_title):
        self.__tournament_title   = tournament_title
        self.__tournamentUUID     = scr.token_hex(nbytes=16)
        self.__currRound          = 1
        self.__player_arr         = []
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
            
