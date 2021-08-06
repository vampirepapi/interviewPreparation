import math
t=int(input())
for i in range(t):
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    arr1=[0]*31
    for x in range(31):
        for y in range(n):
            if(arr[y]%2!=0):
                arr1[x]+=1
            arr[y]//=2;

    ans=0
    for i in arr1:
        ans+=math.ceil(i/k)
    print(ans)