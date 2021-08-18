t=int(input())
for x in range(t):
    n=int(input())
    j=0
    res=0
    v=1
    while(j<n):
        if v%3 != 0 and list(str(v))[-1] != '3':
            res=v
            j=j+1
        v=v+1

    print(res)