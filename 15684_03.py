import copy
import time
start_time = time.time()

line_in = list(map(int,input().split()))
NVert = line_in[0]
NLadder = line_in[1]
NHor = line_in[2]
# print(NVert, NLadder, NHor)

Ladder = [[False]*(NVert-1) for _ in range(NHor)]

for _ in range(NLadder):
    line_in = list(map(int,input().split()))
    Ladder[line_in[0]-1][line_in[1]-1] = True

# print(Ladder)

def PrintLadder():
    Board = [["| "]*NVert for _ in range(NHor)]
    print(len(Board))
    print(len(Board[0]))
    # print(Board)
    for row in range(NHor):
        for col in range(NVert-1):
            if Ladder[row][col]:
                Board[row][col] = "|-"
    for br in Board:
        print("".join(br))

# PrintLadder(Ladder)


def ClimbDown():
    ## Better to sort the ladder a lot before

    # Number_list = list(range(NVert))
    # Org_Number_list = copy.deepcopy(Number_list)

    # for row in range(NHor):
    #     for col in range(NVert-1):
    #         if Ladder[row][col]:
    #             n1 = Number_list[col]
    #             n2 = Number_list[col+1]
    #             Number_list[col] = n2
    #             Number_list[col+1] = n1

    # return Number_list == Org_Number_list
    for start in range(NVert):
        k = start
        for hor in range(NHor):
            if k < NVert-1 and Ladder[hor][k]:
                k=k+1
            elif k > 0 and Ladder[hor][k-1]:
                k=k-1
        if k != start:
            return False
    return True

# ClimbDown(Ladder)

def Check_avail(new_ladder):
    avail = True
    hor = new_ladder[0]
    vert = new_ladder[1]
    if Ladder[hor][vert]:
        avail = False
    else:
        if vert-1 >= 0:
            if Ladder[hor][vert-1]:
                avail = False
        if vert+1 < NVert-1:
            if Ladder[hor][vert+1]:
                avail = False
    return avail
            

GlobalMin = 4
def MakeLadder(NAdd, last_added):
    global GlobalMin

    if NAdd >= GlobalMin:
        return

    # PrintLadder(fLadder)
    # print()

    if ClimbDown():
        GlobalMin = min(GlobalMin, NAdd)

    for hor in range(last_added[0],NHor):
        if hor == last_added[0]:
            vStart = last_added[1]+1
        else:
            vStart = 0

        for vert in range(vStart,NVert-1):
            if Check_avail([hor,vert]):
                Ladder[hor][vert] = True
                MakeLadder(NAdd+1, [hor, vert])
                Ladder[hor][vert] = False


# print(Ladder)
# Ladder2 = [[False]*(NVert-1) for _ in range(NHor)]
# Ladder2[0][0] = True
# PrintLadder(Ladder2)
# print("Start!!")
# print()
# print(ClimbDown(Ladder))
# print(Ladder)

MakeLadder(0, [0, -1])
# MakeLadder(0, Ladder2, [0, -1])

if GlobalMin == 4:
    GlobalMin = -1
print(GlobalMin)

# print("time: ", time.time()-start_time)

