import math
for x in range(int(input())):
    n=int(input())
    val=(0.143*n)**n
    if val - math.floor(val) < 0.5:
        print(math.floor(val))
    else:
        print(math.floor(val)+1)
