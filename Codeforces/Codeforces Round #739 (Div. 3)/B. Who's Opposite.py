def state(statement,one,two):
  print(one if statement else two)
t=int(input())
for x in range(t):
    a,b,c = map(int,input().split())
    limit=2*abs(b-a);
    if(a>limit or b>limit or c>limit):
        print(-1)

    else:
        l=limit//2
        state(c>l,c-l,c+l)