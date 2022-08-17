
Ndays = int(input())
Ti_List = []
Pi_List = []
for _ in range(Ndays):
    Tmp_List = list(map(int,input().split()))
    Ti_List.append(Tmp_List[0])
    Pi_List.append(Tmp_List[1])

MaxPay = 0
def DFS(CDate,TotalPay):
    global Ndays
    global MaxPay

    if TotalPay > MaxPay:
        MaxPay = TotalPay

    if CDate == Ndays+1:
        return

    if CDate+Ti_List[CDate-1] <= Ndays+1:
        ## 그날까진 괜찮
        DFS(CDate+Ti_List[CDate-1],TotalPay+Pi_List[CDate-1])
    if CDate+1 <= Ndays+1:
        DFS(CDate+1,TotalPay)

DFS(1,0)
print(MaxPay)


