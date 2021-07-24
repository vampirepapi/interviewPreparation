def primeFactors(n):         		#O(n)
	for x in range(2,n+1):
		if isPrime(x):				#O(n)
			j = x
			while n%j==0:			#O(logn)
				print(x,end=' ')
				j=j*x


def isPrime(x):
	for i in range(2,int(x**(1/2))+1):
		if x%i == 0:
			return False
	return True

primeFactors(315)


#TC = O(n^2(logn))