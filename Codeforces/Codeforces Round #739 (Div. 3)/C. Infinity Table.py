import math
t=int(input())
for x in range(t):
    n=int(input())
    sqrt=int(math.sqrt(n))
    if(sqrt*sqrt==n): print(sqrt,1)
    else:
      n-=(sqrt*sqrt)
      if n<=sqrt+1: print(n,sqrt+1) 
      else:
        n-=sqrt+1;
        print(sqrt+1,sqrt+1-n)
