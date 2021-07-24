#Simple Brute Force Approach:

def allDivisors(n):
	for i in range(1,n+1):
		if n%i==0:
			print(i,end=' ')
allDivisors(25)

#TC = O(n)


#Approach 2(More Eficient):
def allDivisors(n):
	m=int(n**(0.5))
	for i in range(1,m+1):
		if n%i==0:
			print(i,end=' ')

			if i!=n//i:
				print(n//i,end=' ')

allDivisors(25)

#TC = O(root(n)