# 9. Palindrome Number
# Easy

# 4126

# 1873

# Add to List

# Share
# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

# Example 1:

# Input: x = 121
# Output: true
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Example 4:

# Input: x = -101
# Output: false
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
        	# print(x)
        	return False
        else:
        	temp = x
        	# print('temp',temp)
        	# print('x',x)
        	res = 0
        	while temp>0:
        		rem = temp%10
        		temp = temp //10
        		res = res*10 + rem
        	if res == x:
        		# print('tempif',temp)
        		return True
        	else:
        		return False
p = Solution()
print(p.isPalindrome(1))