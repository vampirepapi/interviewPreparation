#Quick sort approach:-

def qsort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr.pop()

	items_greater = []
	items_lower = []

	for x in arr:
		if x > pivot:
			items_greater.append(x)

		if x < pivot:
			items_lower.append(x)

	#move all -ve nos to the end of arr
	#return qsort(items_greater) + [pivot] + qsort(items_lower) 
	
	#move all -ve nos to the start of arr
	return qsort(items_lower) + [pivot] + qsort(items_greater)  


print(qsort([-1, 2, -3, 4, 5, 6, -7, 8, 9]))

# TC(worst case) = as we used quick sort here so out TC will br:
# 			= O(n**2)


#Best Approach:-
