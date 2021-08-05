# Given a sorted array arr containing n elements with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.

# Example 1:

# Input:
# n=9, x=5
# arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
# Output:  2 5
# Explanation: First occurrence of 5 is at index 2 and last
#              occurrence of 5 is at index 5. 


# Expected Time Complexity: O(logN)
# Expected Auxiliary Space: O(1)

#Naive Approach
arr=[1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x=8
first_idx = -1
last_idx = -1

for i in range(len(arr)):
    if arr[i] == x:
        if first_idx == -1:
            first_idx =i

        last_idx =i
print(first_idx, last_idx)

# Time Complexity: O(n) 
# Auxiliary Space: O(1)


arr=[1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x=8
#Binary Search Approach:-
def binarySearchLast(arr,key):
    low = 0
    high = len(arr) - 1
    found = -1

    while low <= high:
        mid = (low+high)//2
        # if mid == key:
        #     return mid

        if key>arr[mid]:
            low = mid+1

        elif key < arr[mid]:
            high = mid-1

        else:
            found = mid
            low = mid+1 # for last occurence
            #high = mid-1 #for first occurence
    return found


def binarySearchFirst(arr,key):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if key == arr[mid]:
            return mid
        elif key>mid:
            low= mid+1
        else:
            high=mid-1

print(binarySearchFirst(arr,x))
print(binarySearchLast(arr,x))




