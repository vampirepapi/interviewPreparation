# # class Solution(object):
# #    def mctFromLeafValues(self, arr):
# #       """
# #       :type arr: List[int]
# #       :rtype: int
# #       """
# #       self. memo = {}
# #       def dp(i,j):
# #          if j<=i:
# #             return 0
# #          if (i,j) in self.memo:
# #             return self.memo[(i,j)]
# #          res = float('inf')
# #          for k in range(i,j):
# #             res = min(res,dp(i,k) + dp(k+1,j) + (max(arr[i:k+1])*max(arr[k+1:j+1])))
# #          self.memo[(i,j)]=res
# #          return self.memo[(i,j)]
# #       return dp(0,len(arr)-1)


# # p=Solution()
# # print(p.mctFromLeafValues([5,3,1]))
# #     

# # def solution(input_from_question):
# # 	if input_from_question>12 or input_from_question<0:
# # 		return 0
# # 	else:
# # 		return ((input_from_question*(input_from_question+1))//2)**2

# # print(solution(input_from_question))

# array = [12, 3]

# num_special = 0

# for item in array:
#   for num in range(1, item):
#     if (num + int(str(num)[::-1]) == item):
#       num_special += 1
#       break

# print(num_special)


