from collections import deque
import copy


A = [1, 2, 3, 4, 5]
B = copy.deepcopy(A)

if A==B:
    print("Check!")

A[4] = 0
if A==B:
    print("Check 2!")
else:
    print("different!")