#Python Specific
def sort0(arr):
  l=[]
  m=[]
  n=[]
  for x in arr:
    if x == 0:
      l.append(x)
    elif x == 1:
      m.append(x)
    else:
      n.append(x)
  return l + m + n
print(sort0([0,2,2,1,1,0,2,1]))

#TC =O(n)
#SC = O(n)


#General Approach
def Sort012(arr):
  countZero=0
  countOne=0
  countTwo=0

  idx=0
  while idx<len(arr):
    if arr[idx] == 0:
      countZero+=1

    if arr[idx] == 1:
      countOne+=1

    if arr[idx] == 2:
      countTwo+=1

    idx+=1

  countK=0
  popArr=[None] * len(arr)

  for x in range(countZero):
    popArr[countK] = 0
    countK+=1

  for x in range(countOne):
    popArr[countK] = 1
    countK+=1

  for x in range(countTwo):
    popArr[countK] = 2
    countK+=1
  
  return popArr

print(Sort012([0,2,2,1,1,0,2,1]))

#TC =O(n)
#SC = O(n)


#For more optimization we can use :
      #Dutch National Flag Problem
