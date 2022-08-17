from collections import deque
import copy

import time
start = time.time()

Nrow, Ncol = map(int,input().split())
NSafeMax = 0

Board = []
Virus_list = []
for row in range(Nrow):
    Lread = list(map(int,input().split()))
    for vcol, val in enumerate(Lread):
        if val == 2:
            Virus_list.append([row,vcol])
            Lread[vcol] = 0
    Board.append(Lread)
##!# Board itself never changes here below
# print(Virus_list)

def PrintBoard(fWallsAdded, fVirus_list):
    # global Board
    BoardCpy = copy.deepcopy(Board)
    print(fWallsAdded)
    for walls in fWallsAdded:
        BoardCpy[walls[0]][walls[1]] = 3
    for vl in fVirus_list:
        BoardCpy[vl[0]][vl[1]] = 2
    for br in BoardCpy:
        print(" ".join([str(x) for x in br]))


# def PrintBoardTmp(fWallsAdded, fVirus_list, fVirus_update):
#     global Board
#     BoardCpy = copy.deepcopy(Board)
#     print(fWallsAdded)
#     for walls in fWallsAdded:
#         BoardCpy[walls[0]][walls[1]] = 3
#     for vl in fVirus_list:
#         BoardCpy[vl[0]][vl[1]] = 2
#     BoardCpy[fVirus_update[0]][fVirus_update[1]] = 9
#     for br in BoardCpy:
#         print(" ".join([str(x) for x in br]))

def NextSpread(dir, pos):

    if dir == 0:
        pos[1] += 1
    elif dir == 1:
        pos[0] -= 1
    elif dir == 2:
        pos[1] -= 1
    elif dir == 3:
        pos[0] += 1

    return pos

def VirusBFS(fWallsAdded, fVirus_list):
    global NSafeMax
    # global Nrow, Ncol

    # print(fVirus_list)
    # print(fVirus_BFS)
    Board_update = copy.deepcopy(Board)
    for walls in fWallsAdded:
        Board_update[walls[0]][walls[1]] = 1
    for virus in fVirus_list:
        Board_update[virus[0]][virus[1]] = 2
    
    fVirus_BFS = deque(fVirus_list)
    while(fVirus_BFS):
        # row, col = fVirus_BFS.popleft()
        [row, col] = fVirus_BFS.popleft()
        for dir in range(4):
            nrow, ncol = NextSpread(dir, [row, col])
            if nrow >= 0 and nrow < Nrow and ncol >= 0 and ncol < Ncol:
                # print(row, col)
                if Board_update[nrow][ncol] == 0:
                    Board_update[nrow][ncol] = 2
                    fVirus_BFS.append([nrow, ncol])
                    # PrintBoardTmp(fWallsAdded, fVirus_list, [row, col])


    NSafe = CountSafe(Board_update)
    # print("NSafe: "+str(NSafe))
    # print()
    NSafeMax = max(NSafeMax,NSafe)

    return

def CountSafe(Board_update):
    NSafe = 0

    for row in range(Nrow):
        for col in range(Ncol):
            if Board_update[row][col] == 0:
                NSafe += 1

    return NSafe 

def BoardDFS(fWallsAdded, fVirus_list):
    # global Board
    global NSafeMax

    if len(fWallsAdded) == 3:
    #     ## BFS run
        # PrintBoard(fWallsAdded, fVirus_list)
        fVirus_list_update = copy.deepcopy(fVirus_list)
        VirusBFS(fWallsAdded, fVirus_list_update)
        # PrintBoard(fWallsAdded, fVirus_list_update)
        return
    
    if not fWallsAdded:
        raise ValueError("Where are the Additional Walls?")
    
    prevWall = fWallsAdded[-1]
    for row in range(prevWall[0],Nrow):
        if row == prevWall[0]:
            for col in range(prevWall[1]+1,Ncol):
                if (not Board[row][col]) and ([row, col] not in fVirus_list):
                    BoardDFS(fWallsAdded+[[row,col]], fVirus_list)
        else:
            for col in range(Ncol):
                if (not Board[row][col]) and ([row, col] not in fVirus_list):
                    BoardDFS(fWallsAdded+[[row,col]], fVirus_list)


## The First Wall
for row in range(Nrow):
    for col in range(Ncol):
        if (not Board[row][col]) and ([row, col] not in Virus_list):
            # print(row,col)
            BoardDFS([[row,col]], Virus_list)

print(NSafeMax)
# print("time: ", time.time() - start)

# VirusBFS([[5, 6], [6, 5], [7, 4]], deque(Virus_list), Virus_list)

# print(Virus_list)
# Virus_list = deque(Virus_list)
# print(Virus_list)