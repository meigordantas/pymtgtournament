#Player Class

class Player():
    
    def __init__(self, dci_no, player_name):
        self.__player_name = player_name
        self.__dci_no = dci_no
        self.__score = 0                        # Holds its own score,
        self.__win_pct = 0                      # win percentage and
        self.__wdl = {'w': 0, 'd': 0, 'l': 0}   # Win/Draw/Lose
    
    def showWdl(self):
        return("W:%s\tD:%s\tL:%s" %(self.__wdl['w'], self.__wdl['d'], self.__wdl['l']))
    
    def getPlayerName(self):
        return self.__player_name
    
    def getPlayerDci(self):
        return self.__dci_no
    
    def getScore(self):
        return self.__score
    
    def getWinPct(self):
        return self.__score
    
    def getPlayerStatistics(self):
        return("W:%s\tD:%s\tL:%s\n\b Score:%s" %(self.__wdl['w'], self.__wdl['d'], self.__wdl['l'], self.__score))