# 1. Two Sum
# Easy

# 25237

# 821

# Add to List

# Share
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
        	for j in range(i+1,len(nums)):
        		if nums[i]+nums[j] == target:
        			return (i,j)

p = Solution()
p.Solution([2,7,11,15],9)



#Optimized Solution:-

# In this approach, we will use the fact that if we fix one of the numbers, say x, we will have to scan the entire array to find the next number y which is (target - x). To do so, we have first declared a dictionary. Then, we will traverse over the entire array and as soon as we find that the corresponding element is present in dictionary that satisfies the condition, we will return it in the form of list. Dry running this code will be helpful to you all for better clarity.

# Time Complexity - O(N)
# Space Complexity - O(N)

# Note - I am a little confused with regards to the Time Complexity consumed in the if nums[i] in dic statement as statements on Internet varies, feel free to correct me here.

# //Answered below

# Explanation : if nums[i] in dic: It is not O(N) as dic is not representing an array, but a dictionary.

# Dictionary works like a map. There are two kinds of maps - Unordered and Ordered. Dictionaries are unordered, and Unordered has O(1) time when we are trying to search for an element.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	hash = {}

    	for i in range(len(nums)):
    		if nums[i] in hash:
    			return [hash[nums[i]], i]

    		else:
    			hash [target - nums[i]] = i
        