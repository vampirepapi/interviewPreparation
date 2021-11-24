t=int(input())
for x in range(t):
	n=int(input())
	speeds=list(map(int,input().split()))
	min=speeds[0]
	count=1
	for x in speeds:
		if x<min:
			count+=1
			min=x
	print(count)