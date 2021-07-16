#iterative way
def dig(n):    
    count=0
    while n!=0:
        n=n//10
        count+=1
    return count

print(dig(12345))

#logarithmic way
import math
print(math.floor(math.log10(n)+1))
