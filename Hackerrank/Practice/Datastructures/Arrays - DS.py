def reverseArray(a):
    # Write your code here
    start=0
    end=len(a)-1
    while start < end:
        a[start],a[end] =a[end],a[start]
        start+=1
        end-=1
    return a 

print(reverseArray([1,2,4]))