def solve():
  len=int(input())
  s=input()
  t=input()
  if s==t:
    print("YES")
    return
  couOne=0;
  couTwo=0;
  for _ in range(len):
    if t[_]=="1":
      couOne+=1
    else:
      couTwo+=1
  print("YES" if couOne and couTwo else "NO")

if __name__ == '__main__':
  for i in range(int(input())):
    solve()