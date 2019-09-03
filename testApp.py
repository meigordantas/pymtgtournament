from Matchup import *
from Player import *
from Tournament import *
import random as rnd

arr = []
score = 0
arr.append(Player(12354, 'Player_C'))
arr.append(Player(12345, 'Player_A'))
arr.append(Player(54321, 'Player_B'))
arr.append(Player(15675, 'Player_D'))
arr.append(Player(12342, 'Player_E'))
arr.append(Player(78940, 'Player_F'))

mu = []
for i in range (0,len(arr)//2):
    mu.append(Matchup(arr.pop(0), arr.pop(1), 1))

for i in mu:
    i.getPlayers()
#
# for m in mu:
#     print (m.getPlayers())


