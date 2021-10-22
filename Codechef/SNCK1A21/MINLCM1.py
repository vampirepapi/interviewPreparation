for _ in range(int(input())):
	x,y = map(int,input().split())
	sol = (x*2,(x*y)*((x*y)-1))
	print(*sol)
