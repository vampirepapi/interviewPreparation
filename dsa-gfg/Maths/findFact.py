#iterative approach -- most stable approach
def findFactorial(n):
	d=1
	for x in range(2,n+1):
		d=x*d
	return d

print(findFactorial(5))

#TC = theta(n)
#SC = O(1)



#recursive approach
def fact(n):
	if n==0: return 1
	return n*fact(n-1)

print(fact(5))

#TC = theta(n)
#SC = O(n)