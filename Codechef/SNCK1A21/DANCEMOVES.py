for _ in range(int(input())):
    x,y=map(int,input().split())
    move=0
    while x!=y:
        if x<y:
            x+=2
            move+=1
        else:
            x-=1
            move+=1

    print(move)


