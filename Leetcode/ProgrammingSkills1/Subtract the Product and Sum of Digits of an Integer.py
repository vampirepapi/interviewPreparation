def subtractProductAndSum(n):
    sum=0
    product=1
    while n!=0:
        rem=n%10
        # print("n",n)
        # print("rem",rem)
        sum+=rem
        product*=rem
        n=n//10
    # print(product)
    # print(sum)
    return (product-sum)
print(subtractProductAndSum(4421))
