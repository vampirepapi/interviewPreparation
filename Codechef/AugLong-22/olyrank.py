t=int(input())
for x in range(t):
    arr = list(map(int,input().split()))
    if arr[0]+arr[1]+arr[2] > arr[3]+arr[4]+arr[5]:
        print(1)
    else:
        print(2)