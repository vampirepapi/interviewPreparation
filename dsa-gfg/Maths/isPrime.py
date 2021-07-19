#Basic Approach:-
def isPrime(n):
  if n==1:
    return False
  for x in range(2,(n//2)+1):
    if n%x==0:
      return False

  return True

for x in range(1,50):
  print(x,isPrime(x))

# TC = loop will run (n/2) times in worst case
#  so, TC = O(n)


#Optimized Approach:-
def isPrime(n):
  if n==1:
    return False
  for x in range(2,int(n**(1/2))+1):
    if n%x==0:
      return False

  return True

for x in range(1,50):
  print(x,isPrime(x))

#TC = O(root(n))


#More Optimized Approach:-

