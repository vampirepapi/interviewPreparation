#Approach 1:
def findFactorial(n):
  d=1
  for x in range(2,n+1):
      d=x*d
  return d

num= findFactorial(17)
count = 0

while num%10==0: #checking if rem comes 0 or not
  count+=1
  num=num//10
print(count)

#TC = theta(n) + less(theta(n)) = theta(n)


#Approach 2:(Eficient Approach)

'''
Trailing 0s in n! = Count of 5s in prime factors of n!
                  = floor(n/5) + floor(n/25) + floor(n/125) + ....
'''

def findFactorial(n):
    count = 0
    if n<1:
        return -1
    while (n>=5):
        n=n//5
        count+=n
    return count

print(findFactorial(17))

#TC = theta(logn)
# 5^k <= n
# k<= log(base5)n