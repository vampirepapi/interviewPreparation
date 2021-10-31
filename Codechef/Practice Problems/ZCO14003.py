t=int(input())
buyers=[]
revenues=[]
for _ in range(t):
	x=int(input( ))
	buyers.append(x)
# c=[40,3,65,33,21]
buyers.sort()
# new=[]
n=len(buyers)
for x in range(n):
	revenues.append(buyers[x]*(n-x))
print(max(revenues))