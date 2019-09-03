from Player import *
from Tournament import *
from Matchup import *
#
# t = Tournament('Torneio teste 1')
# print(t.showTournamentUUID())
#
# t.addPlayer(Player(12345,'igor'))
# t.addPlayer(Player(54321,'falcao'))
# t.addPlayer(Player(15432,'Silvio'))
#
# print(t._Tournament__player_arr)
#
# print('Showing players')
# t.showPlayers()
# t.updateCurrScoreBoard()
# print('Showing current scoreboard')
# t.showCurrScoreBoard()

playera = Player(12345,'Player_A')
playerb = Player(54321,'Player_B')
mt = Matchup(playera, playerb, 1)
mt.getPlayers()

try:
    mt.setWinner(0)
except ValueError as err:
    print(err)

if mt.getWinner() == None:
    print("Draw")
else:
    print("Winner is: %s" % (mt.getWinner().getPlayerName()))

