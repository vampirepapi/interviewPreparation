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
