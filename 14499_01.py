
Input_list = list(map(int,input().split()))
Board_size = Input_list[0:2]
Dice_pos = Input_list[2:4]
Board = []
for _ in range(Input_list[0]):
    Board.append(list(map(int,input().split())))
Order_list = list(map(int,input().split()))
Dice = [0]*6

def PrintBoard(Board):
    for br in Board:
        print(" ".join([str(x) for x in br]))
    print()

def RollDice(Dir, Dice):
    if Dir == 1:
        NewDice = [Dice[4 -1],Dice[2 -1],Dice[1 -1],Dice[6 -1],Dice[5 -1],Dice[3 -1]]
    elif Dir == 2:
        NewDice = [Dice[3 -1],Dice[2 -1],Dice[6 -1],Dice[1 -1],Dice[5 -1],Dice[4 -1]]
    elif Dir == 3:
        NewDice = [Dice[5 -1],Dice[1 -1],Dice[3 -1],Dice[4 -1],Dice[6 -1],Dice[2 -1]]
    elif Dir == 4:
        NewDice = [Dice[2 -1],Dice[6 -1],Dice[3 -1],Dice[4 -1],Dice[1 -1],Dice[5 -1]]
    else:
        raise ValueError("Dir is not btw 1 and 4: "+str(Dir))
    return NewDice

drow = [0, 0, -1, +1] 
dcol = [+1, -1, 0, 0]
## 동서북남

for order in Order_list:
    Next_Row = Dice_pos[0]+drow[order -1]
    Next_Col = Dice_pos[1]+dcol[order -1]

    # print(Next_Row, Next_Col)

    if Next_Row < 0 or Next_Row >= Board_size[0]:
        continue
    if Next_Col < 0 or Next_Col >= Board_size[1]:
        continue

    Dice_pos = [Next_Row, Next_Col]
    Dice=RollDice(order,Dice)

    if Board[Next_Row][Next_Col] == 0:
        Board[Next_Row][Next_Col] = Dice[6 -1]
    else:
        Dice[6 -1] = Board[Next_Row][Next_Col]
        Board[Next_Row][Next_Col] = 0

    print(Dice[1 -1])

