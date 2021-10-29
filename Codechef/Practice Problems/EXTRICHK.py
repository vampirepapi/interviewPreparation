a,b,c = map(int,input().split())
if (a+b<=c) or (b+c<=a) or (c+a<=b):
	print("-1")
else:
	if a==b==c:
		print(1)
	elif a!=b and b!=c and c!=a:
		print(3)
	else:
		print(2)