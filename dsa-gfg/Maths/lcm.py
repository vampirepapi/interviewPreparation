# as we know that (a*b) = gcd(a,b) * lcm(a,b) 
# so from above formula we can calculate lcm
#               = [ lcm(a,b) = (a*b) / gcd(a,b) ]


def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(b,a%b)

def lcm(a,b):
  return (a*b)//gcd(a,b)

print(lcm(2,5))


# TC = gcd TC i.e log(min(a,b)) + some theta constant work for lcm return
# so,   
# TC  = O(log(min(a,b)))