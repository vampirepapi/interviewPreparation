for _ in range(int(input())):
   x,y =  map(int,input().split())
   k=x-y
   if y==1:
      # print("qst")
      print((x-1)*2)
   
   elif y>2:
      # print(y)
      if y%2==1:
         # print(y&1)
         print(2*k+(y//2)*2)
      else:
         # print("else")
         print(2*k+(y//2-1)*2)
   else:
      # print("last")
      print(2*k)
