n=int(input())
allNos = list(map(int,input().split()))
print(*allNos[::-1],sep=' ')