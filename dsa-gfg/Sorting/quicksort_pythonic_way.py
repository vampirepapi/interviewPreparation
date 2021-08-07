def quick_sort(arr):
	length = len(arr)

	if length < 1:
		return arr

	else:
		pivot = arr.pop()

	items_grtr = []
	items_lowr = []

	for x in arr:
		if x > pivot:
			items_grtr.append(x)
		else:
			items_lowr.append(x)

	return quick_sort(items_lowr) + [pivot] + quick_sort(items_grtr)

arr = [10, 7, 8, 9, 1, 5] 

print(quick_sort(arr)) 

