def bubble_sort(arr):
	n = len(arr)

	for i in range(n):
		swapped = False

		for j in range(0,n-i-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]

				swapped = True

		if swapped == False:
			break

	return arr


arr = [10, 7, 8, 9, 1, 5] 
print(bubble_sort(arr)) 

#TC = O(n**2)
#TC = O(n) [Best Case when arr is already sorted]


