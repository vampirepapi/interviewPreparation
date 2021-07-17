def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        # print("pvt",pivot)
        # print('seq',sequence)

    items_greater = []
    items_lower = []

    for item in sequence:
        # print('item',item)
        # print('pivot',pivot)
        if item > pivot:
            items_greater.append(item)
            # print('gtrt item', item)

        else:
            items_lower.append(item)
            # print('lwr item', item)



    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

arr=[7,10,4,3,20,15]
sort_arr = quick_sort(arr)
k=3
print(sort_arr)
print(sort_arr[k-1])

#YT link - https://www.youtube.com/watch?v=kFeXwkgnQ9U&ab_channel=DerrickSherrill