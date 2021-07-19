#Naive Approach:-
def gcd(a, b):
  if a>b:
    small = b
  else:
    small = a
  while small>0:
    if a%small == 0 and b%small == 0:
      break
    small-=1
  return small 
print(gcd(4, 6))

#TC= O(min(a,b))

# Euclidean Algorithm:
# if b is smaller than a ,
# gcd(a,b) = gcd(a-b,b)

#Basic Eucledian Approach:-
def gcd(a,b):
  while a!=b:
    if a>b:
      a=a-b
    else:
      b=b-a
  return a
print(gcd(4, 6))

#Optimized Eucledian Approach(Best Approach):-
def gcd (a,b):
  if b==0:
    return a
  else:
    return gcd(b, a%b)

print(gcd(4, 20))
  
#TC = log(min(a,b))