Ndays = int(input())
Ti_List = []
Pi_List = []
for _ in range(Ndays):
    Tmp_List = list(map(int,input().split()))
    Ti_List.append(Tmp_List[0])
    Pi_List.append(Tmp_List[1])

DynM = [0]*(Ndays+1)
## Maximum payment at Day i

for day in range(Ndays):

    if day+1 <= Ndays:
        ## (Ndays+1) -1 for index
        DynM[day+1] = max(DynM[day+1], DynM[day])
    if day+Ti_List[day] <= Ndays:
        DynM[day+Ti_List[day]] = max(DynM[day+Ti_List[day]], DynM[day]+Pi_List[day])

print(DynM[-1])


