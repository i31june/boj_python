
NPeople = int(input())

Syn_mat = []
for _ in range(NPeople):
    Syn_mat.append(list(map(int,input().split())))

Global_Min = 2100000000
def Cal_Power(fStart_list):
    global Global_Min
    # print(fStart_list)
    Start_Power = 0
    Link_Power = 0
    for i in range(NPeople):
        for j in range(NPeople):
            if i in fStart_list and j in fStart_list:
                Start_Power += Syn_mat[i][j]
            if i not in fStart_list and j not in fStart_list:
                Link_Power += Syn_mat[i][j]
    # print(Start_Power, Link_Power)
    Global_Min = min(Global_Min, abs(Start_Power-Link_Power))

def DFS(fStart_list, last_pick):

    if len(fStart_list) == NPeople/2:
        Cal_Power(fStart_list)

    for next_pick in range(last_pick+1,NPeople):
        fStart_list.append(next_pick)
        DFS(fStart_list, next_pick)
        fStart_list.pop()

DFS([],-1)

print(Global_Min)