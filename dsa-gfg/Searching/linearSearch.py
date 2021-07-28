def linearSearch(arr,key):
    for x in range(len(arr)):
        if arr[x] == key:
            return x

    return -1


print(linearSearch([2,1,4,5645,6,34,3634,4], 40))


# TC = theta(n) 
# SC = theta(1)