
from Player import *
from Tournament import *

t = Tournament('Torneio teste 1')
print(t.showTournamentUUID())

t.addPlayer(Player(12345,'igor'))
t.addPlayer(Player(54321,'falcao'))
t.addPlayer(Player(15432,'Silvio'))

print(t._Tournament__player_arr)

print('Showing players')
t.showPlayers()
t.updateCurrScoreBoard()
print('Showing current scoreboard')
t.showCurrScoreBoard()
