for x in range(int(input())):
    x,y,z = map(int,input().split())
    AmountSpent = x*y
    SellingPrice = x*z
    profit = SellingPrice - AmountSpent 
    print(profit)
