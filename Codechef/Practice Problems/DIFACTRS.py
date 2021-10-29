n=int(input())
allFactors=[]
for x in range(1,n+1):
	if n%x==0:
		allFactors.append(x)
print(len(allFactors))
print(*allFactors, sep=' ')
