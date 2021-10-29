l,r = map(int,input().split())
oddNums=[]
for x in range(l,r+1):
	if x%2==1:
		oddNums.append(x)

print(*oddNums,sep=' ')
