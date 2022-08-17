
NNumber = int(input())
Num_in = list(map(int,input().split()))
Oper_avail = list(map(int,input().split()))

Global_Min = 1000000001
Global_Max = -1000000001

def Commit_Oper(fOper_list):
    global Global_Min
    global Global_Max

    oper_result = Num_in[0]
    for i in range(len(fOper_list)):
        if fOper_list[i] == 0:
            oper_result += Num_in[i+1]
        elif fOper_list[i] == 1:
            oper_result -= Num_in[i+1]
        elif fOper_list[i] == 2:
            oper_result *= Num_in[i+1]
        elif fOper_list[i] == 3:
            oper_result = int(oper_result/Num_in[i+1])
        else:
            raise ValueError("Operation not between 0 and 3: "+str(fOper_list[i]))
    
    Global_Min = min(Global_Min, oper_result)
    Global_Max = max(Global_Max, oper_result)


def DFS_Oper(fOper_list,fOper_used):

    if fOper_used == Oper_avail:
        Commit_Oper(fOper_list)
        return

    for oper in range(4):
        if fOper_used[oper] == Oper_avail[oper]:
            continue
        else:
            fOper_list.append(oper)
            fOper_used[oper] += 1
            DFS_Oper(fOper_list,fOper_used)
            fOper_list.pop()
            fOper_used[oper] -= 1

Oper_used = [0]*4
DFS_Oper([],Oper_used)

print(Global_Max)
print(Global_Min)