import time
start_time = time.time()

line_in = list(map(int,input().split()))
NVert = line_in[0]
NLadder = line_in[1]
NHor = line_in[2]
# print(NVert, NLadder, NHor)

Ladder = []
for _ in range(NLadder):
    Ladder.append(list(map(int,input().split())))

def PrintLadder():
    Board = [["| "]*NVert for _ in range(NHor)]
    # print(Board)
    for ld in Ladder:
        Board[ld[0]-1][ld[1]-1] = "|-"
    for br in Board:
        print("".join(br))

def ClimbDown():
    ## Better to sort the ladder a lot before
    # Ladder_cpy = copy.deepcopy(Ladder)
    # Ladder_cpy.sort()

    # Number_list = list(range(NVert))
    # Org_Number_list = copy.deepcopy(Number_list)

    # for ld in Ladder_cpy:
    #     # print(ld)
    #     n1 = Number_list[ld[1]-1]
    #     n2 = Number_list[ld[1]]
    #     Number_list[ld[1]-1] = n2
    #     Number_list[ld[1]] = n1

    # return Number_list == Org_Number_list

    # print(Ladder)
    # PrintLadder(Ladder)

    for start in range(1,NVert+1):
        k = start
        for hor in range(1,NHor+1):
            # print(k, hor)
            if [hor,k] in Ladder:
                k=k+1
            elif [hor,k-1] in Ladder:
                k=k-1
        if k != start:
            return False
    return True    



GlobalMin = 4
def MakeLadder(NAdd, last_added):
    global GlobalMin

    if NAdd >= GlobalMin:
        return

    # PrintLadder()
    # print()

    if ClimbDown():
        GlobalMin = min(GlobalMin, NAdd)

    hor = last_added[0]
    for vert in range(last_added[1]+1,NVert+1-1):
        if [hor, vert] not in Ladder and [hor, vert-1] not in Ladder and [hor, vert+1] not in Ladder:
            # print([hor, vert])
            Ladder.append([hor, vert])
            MakeLadder(NAdd+1, [hor, vert])
            Ladder.pop()
    for hor in range(last_added[0]+1,NHor+1):
        for vert in range(1,NVert+1-1):
            if [hor, vert] not in Ladder and [hor, vert-1] not in Ladder and [hor, vert+1] not in Ladder:
                # print([hor, vert])
                Ladder.append([hor, vert])
                MakeLadder(NAdd+1, [hor, vert])
                Ladder.pop()

# print(Ladder)
# Ladder = [[5,4]]
# PrintLadder(Ladder)
# print()
# print(ClimbDown(Ladder))
# print(Ladder)

MakeLadder(0, [1, 0])

if GlobalMin == 4:
    GlobalMin = -1
print(GlobalMin)

# print("time: ", time.time()-start_time)