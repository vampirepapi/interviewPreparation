# # # def partition(arr, low , high):
# # #     i = (low-1)
# # #     pivot = arr[high]

# # #     for j in range (low,high):
# # #         if arr[j]<= pivot:
# # #             i=i+1
# # #             arr[i],arr[j]=arr[j],arr[i]
# # #     arr[i+1],arr[high] = arr[high],arr[i+1]
# # #     return (i+1)

# # # def quickSort(arr,low,high):

# # #     if low<high:
# # #         pi = partition(arr,low,high)

# # #         quickSort(arr,low,pi-1)
# # #         quickSort(arr,pi+1,high)
# # #     return arr


# # # # Driver code to test above 
# # # arr = [10, 7, 8, 9, 1, 5] 
# # # n = len(arr) 
# # # print(quickSort(arr,0,n-1)) 





# # def partition(arr, low , high):
# #     i = low-1
# #     pivot = arr[high]

# #     for j in range (low,high):
# #         if arr[j]<=pivot:
# #             i=i+1
# #             arr[i],arr[j]= arr[j],arr[i]

# #     arr[i+1],arr[high] = arr[high],arr[i+1]
# #     return i+1

# # def quickSort(arr,low,high):
# #     if low<high:
# #         pi = partition(arr,low,high)
# #         quickSort(arr,low,pi-1)
# #         quickSort(arr,pi+1,high)
# #     return(arr)

# # arr = [10, 7, 8, 9, 1, 5]
# # n = len(arr) 
# # print(quickSort(arr,0,n-1)) 





# # def partition(arr,low,high):
# #     i=low-1
# #     pivot = arr[high]

# #     for j in range(low,high):
# #         if arr[j] <= pivot:
# #             i=i+1
# #             arr[i],arr[j] = arr[j],arr[i]

# #     arr[i+1],arr[high] = arr[high], arr[i+1]
# #     return i+1

# # def quickSort(arr,low,high):
# #     if low < high:
# #         pi = partition(arr,low,high)
# #         quickSort(arr,low,pi-1)
# #         quickSort(arr,pi+1,high)
# #     return arr

# # arr = [1, 7, -8, 9, 0, 5]
# # n = len(arr) 
# # print(quickSort(arr,0,n-1)) 




# # Python program for implementation of MergeSort
# def mergeSort(arr):
#     if len(arr) > 1:

#         # Finding the mid of the array
#         mid = len(arr)//2

#         # Dividing the array elements
#         L = arr[:mid]

#         # into 2 halves
#         R = arr[mid:]

#         # Sorting the first half
#         mergeSort(L)

#         # Sorting the second half
#         mergeSort(R)

#         i = j = k = 0

#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1

#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
#     return arr

# # Code to print the list



# # Driver Code
# arr = [12, 11, 13, 5, 6, 7]
# print(mergeSort(arr))
    
# # This code is contributed by Mayank Khanna




