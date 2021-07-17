#iterative way --1
def dig(n):    
    count=0
    while n!=0:
        n=n//10
        count+=1
    return count

print(dig(12345))

#TC = theta(d)  where d = number of digits




#logarithmic way --2
import math
print(math.floor(math.log10(n)+1))



#recursive way --3
def dig(n):
    if n==0:
        return 0

    return 1 + dig(n//10)

print(dig(123))
