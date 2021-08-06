t=int(input())
for _ in range(t):
	d,x,y,z = map(int,input().split())
	c=(x*7)
	d=(y*d)+z*(7-d)
	# print(c)
	# print(d)
	print(max(c,d))