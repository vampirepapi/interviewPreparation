n=int(input())
oddNums=[]
evenNums=[] 
for num in range(1,n*2+1,2):
    oddNums.append(num)
for num in range(2,n*2+1,2):
    evenNums.append(num)
print(sum(oddNums),sum(evenNums))