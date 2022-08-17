from collections import deque
import copy

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
    global Board
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

def VirusBFS(BoardUpdate, fVirus_BFS, fVirus_list):
    global Nrow, Ncol

    # print(fVirus_list)
    # print(fVirus_BFS)
    while(fVirus_BFS):
        BFSelt = fVirus_BFS.popleft()
        for dir in range(4):
            row, col = NextSpread(dir, copy.deepcopy(BFSelt))
            if row >= 0 and row < Nrow and col >= 0 and col < Ncol:
                # print(row, col)
                if (not Board[row][col]) and ([row, col] not in fWallsAdded) and ([row, col] not in fVirus_list):
                    fVirus_list.append([row, col])
                    fVirus_BFS.append([row, col])
                    # PrintBoardTmp(fWallsAdded, fVirus_list, [row, col])

    return

def CountSafe(fWallsAdded, fVirus_list_update):
    global Nrow
    global Ncol

    NSafe = 0

    for row in range(Nrow):
        for col in range(Ncol):
            if (Board[row][col] == 0) and ([row, col] not in fWallsAdded) and ([row, col] not in fVirus_list_update):
                NSafe += 1

    return NSafe 


def BoardDFS(fWallsAdded, fVirus_list):
    global Board
    global NSafeMax

    if len(fWallsAdded) == 3:
    #     ## BFS run
        # PrintBoard(fWallsAdded, fVirus_list)
        fVirus_list_update = copy.deepcopy(fVirus_list)
        Board_update = copy.deepcopy(Board)
        for new_wall in fWallsAdded:
            Board_update[new_wall[0]][new_wall[1]] = 1
        # VirusBFS(Board_update, deque(fVirus_list_update), fVirus_list_update)
        PrintBoard(fWallsAdded, fVirus_list_update)
        NSafe = CountSafe(fWallsAdded, fVirus_list_update)
        # print("NSafe: "+str(NSafe))
        # print()
        NSafeMax = max(NSafeMax,NSafe)
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
# for row in range(Nrow):
#     for col in range(Ncol):
#         if (not Board[row][col]) and ([row, col] not in Virus_list):
#             # print(row,col)
#             BoardDFS([[row,col]], Virus_list)


def MakeWalls(fWallsAdded, fVirus_list):
    global Board
    global Nrow
    global Ncol
    global NSafeMax


    if len(fWallsAdded) == 3:
   #     ## BFS run
        PrintBoard(fWallsAdded, fVirus_list)
        fVirus_list_update = copy.deepcopy(fVirus_list)
        VirusBFS(fWallsAdded, deque(fVirus_list_update), fVirus_list_update)
        # PrintBoard(fWallsAdded, fVirus_list_update)
        NSafe = CountSafe(fWallsAdded, fVirus_list_update)
        # print("NSafe: "+str(NSafe))
        # print()
        NSafeMax = max(NSafeMax,NSafe)
        return

    for row in range(Nrow):
        for col in range(Ncol):
            if row >= 0 and row < Nrow and col >= 0 and col < Ncol:          
                if Board[row][col] == 0 and [row, col] not in fWallsAdded and [row,col] not in fVirus_list:
                    MakeWalls(fWallsAdded+[[row, col]], fVirus_list)  

MakeWalls([], Virus_list)

print(NSafeMax)

# VirusBFS([[5, 6], [6, 5], [7, 4]], deque(Virus_list), Virus_list)

# print(Virus_list)
# Virus_list = deque(Virus_list)
# print(Virus_list)