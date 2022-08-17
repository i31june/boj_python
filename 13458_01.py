NPlace = int(input())
NPeople = list(map(int,input().split()))
NSupervisor = list(map(int,input().split()))

# print(NSupervisor)
# print(NPeople)

NAltNeed = 0
for np in NPeople:
    if np-NSupervisor[0] >= 0:
        NAltNeed += (np-NSupervisor[0]-1)//NSupervisor[1]+1
    ## 위의 if 문이 없으면 통과 못함. 반례: 인원 10, 주감독 100명, 보조감독 1명 의 케이스

print(NPlace+NAltNeed)

