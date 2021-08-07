def selection_sort(arr):
	n = len(arr)

	for i in range(n):
		min_idx = i

		for j in range(i+1,n):
			if arr[min_idx] > arr[j]:
				min_idx = j

		arr[i],arr[min_idx] = arr[min_idx],arr[i]

	return arr

arr = [10, 7, 8, 9, 1, 5] 
print(selection_sort(arr)) 

# Time Complexity: O(n2) as there are two nested loops.
# Auxiliary Space: O(1) 

