def findMinMax(arr):
    max=min = arr[0]

    for x in range(len(arr)):
        if arr[x] > max:
            max = arr[x]

        elif arr[x] < min:
            min = arr[x]
    return max , min

print(findMinMax([5,9]))


