
from itertools import dropwhile


Nrow, Ncol = map(int, input().split())
line_tmp = list(map(int, input().split()))
Rpos = line_tmp[0:2]
Rdir = line_tmp[2]

Board = []
for row in range(Nrow):
    Board.append(list(map(int, input().split())))

def PrintBoard(Board):
    for row in Board:
        print(" ".join([str(x) for x in row]))

def LeftTurn(dir):
    ndir = 0
    if dir == 0:
        ndir = 3
    elif dir == 1:
        ndir = 0
    elif dir == 2:
        ndir = 1
    elif dir == 3:
        ndir = 2
    return ndir

drow = [ -1, 0, +1, 0]
dcol = [ 0, +1, 0, -1]

NCleaned = 0
while(1):
    if Board[Rpos[0]][Rpos[1]] == 0:
        Board[Rpos[0]][Rpos[1]] = 2
        NCleaned += 1
    else:
        tf_move = 0
        for _ in range(4):
            Rdir = LeftTurn(Rdir)
            nRpos = [Rpos[0]+drow[Rdir], Rpos[1]+dcol[Rdir]]
            if Board[nRpos[0]][nRpos[1]] == 0:
                Rpos = [nRpos[0], nRpos[1]]
                Board[Rpos[0]][Rpos[1]] = 2
                tf_move = 1
                NCleaned += 1
                break
        if tf_move == 0:
            nRpos = [Rpos[0]-drow[Rdir], Rpos[1]-dcol[Rdir]]
            if Board[nRpos[0]][nRpos[1]] == 1:
                break
            else:
                Rpos = [nRpos[0], nRpos[1]]


# print(Rpos)
# PrintBoard(Board)
print(NCleaned)





