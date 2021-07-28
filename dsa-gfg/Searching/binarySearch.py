def binarySearch(arr,key):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)//2

        if arr[mid] == key:
            return mid
        if key > arr[mid]:
            low = mid+1
        else:
            high = mid -1
    return -1

print(binarySearch([2, 3, 4, 10, 40], 41))