from collections import deque

dRow = [ 0, -1, 0, +1]
dCol = [ +1, 0, -1, 0]

NBoard = int(input())
NApple = int(input())


def m1(in1):
    return in1-1

Apple_list = []
for _ in range(NApple):
    Apple_list.append(list(map(m1,map(int,input().split()))))
## 

NRot = int(input())
Rot_Time = deque()
Rot_Steer = deque()
for _ in range(NRot):
    Tmp_List = list(input().split())
    Rot_Time.append(int(Tmp_List[0]))
    Rot_Steer.append(Tmp_List[1])

# print(Apple_list)
# print(Rot_Time)
# print(Rot_Steer)

def Rotate(run_dir, rot_dir):
    if run_dir == 0:
        if rot_dir == 'L':
            next_dir = 1
        elif rot_dir == 'D':
            next_dir = 3
    if run_dir == 1:
        if rot_dir == 'L':
            next_dir = 2
        elif rot_dir == 'D':
            next_dir = 0
    if run_dir == 2:
        if rot_dir == 'L':
            next_dir = 3
        elif rot_dir == 'D':
            next_dir = 1
    if run_dir == 3:
        if rot_dir == 'L':
            next_dir = 0
        elif rot_dir == 'D':
            next_dir = 2

    # if rot_dir == 'L':
    #     next_dir = (run_dir+1) % 4
    # elif rot_dir == 'D':
    #     next_dir = (run_dir+3) % 4

    return next_dir
        
def PrintSnake(Snake, Apple_list):
    global NBoard
    Board = [["_"]*NBoard for _ in range(NBoard)]
    for sn in Snake:
        Board[sn[0]][sn[1]] = "o"
    for ap in Apple_list:
        Board[ap[0]][ap[1]] = "A"
    for br in Board:
        print("".join(br))
    print()


dir = 0
Snake = deque()
Snake.append([0, 0])

TRun = 0
Run_Dir = 0
# for _ in range(5):
while(1):
    # PrintSnake(Snake, Apple_list)
    TRun += 1
    Row_Next = Snake[-1][0] + dRow[Run_Dir]
    Col_Next = Snake[-1][1] + dCol[Run_Dir]
    if Row_Next < 0 or Row_Next >= NBoard:
        break
    elif Col_Next < 0 or Col_Next >= NBoard:
        break
    elif [Row_Next,Col_Next] in Snake:
        break

    Snake.append([Row_Next,Col_Next])

    if Snake[-1] in Apple_list:
        Apple_list.remove(Snake[-1])
    else: 
        Snake.popleft()
    
    Next_Dir = Run_Dir
    if Rot_Time:
        if TRun == Rot_Time[0]:
            Rot_Time.popleft()
            Rot_Dir = Rot_Steer.popleft()
            Next_Dir = Rotate(Run_Dir, Rot_Dir)
    Run_Dir = Next_Dir



print(TRun)