#Sieve of Eratothenes:-
from math import *
def SieveofEratothenes(n):
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    for p in range(2,int(sqrt(n))+1):
        if primes[p] == True:
            for i in range(p*p,n+1,p):
                primes[i] = False

            
    for i in range(0,len(primes)):
        if primes[i] == True:
            print(i,end=" ")


SieveofEratothenes(150)

#TC = O(nloglog(n))


# #Basic Approach:-
# def isPrime(n):
#   if n==1:
#     return False
#   for x in range(2,(n//2)+1):
#     if n%x==0:
#       return False

#   return True

# def printPrimes(y):
# 	for x in range(1,y+1):
# 		if isPrime(x):
# 			print(x,end=' ')

# printPrimes(10)

# #TC = O(n*n)

