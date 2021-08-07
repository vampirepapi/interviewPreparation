# MergeSort(arr[], l,  r)
# If r > l
#      1. Find the middle point to divide the array into two halves:  
#              middle m = l+ (r-l)/2
#      2. Call mergeSort for first half:   
#              Call mergeSort(arr, l, m)
#      3. Call mergeSort for second half:
#              Call mergeSort(arr, m+1, r)
#      4. Merge the two halves sorted in step 2 and 3:
#              Call merge(arr, l, m, r)

def merge_sort(arr):
		if len(arr) > 1:
			mid = len(arr)//2

			l = arr[:mid]
			r = arr[mid:]

			merge_sort(l)
			merge_sort(r)

			i = j = k = 0

			while i<len(l) and j<len(r):
				if l[i] < r[j]:
					arr[k] = l[i]
					i=i+1

				else:
					arr[k] = r[j]
					j=j+1
				
				k=k+1

			while i<len(l):
				arr[k] = l[i]
				i=i+1
				k=k+1

			while j<len(r):
				arr[k] = r[j]
				j=j+1
				k=k+1

		return arr


arr = [10, 7, 8, 9, 1, 5] 
print(merge_sort(arr)) 

# Time Complexity: O(nlogn)
# Auxiliary Space: O(n) 


