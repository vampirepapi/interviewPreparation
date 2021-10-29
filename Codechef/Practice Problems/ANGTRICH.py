a,b,c = map(int,input().split())
sum = a+b+c
if sum==180 and a>0 and b>0 and c>0:
	print("YES")
else:
	print("NO")