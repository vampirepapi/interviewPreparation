# class Solution:
#     def solve(self, n):
#         while True:
#             n = sum([int(i) ** 2 for i in str(n)])
#             if n == 1:
#                 print("yes")
#             if n == 4:
#                 print("no")

# # res = Solution()  --> creating insctance of a class
# # res.solve(10)  --> calling function from a class
# Solution().solve(10)

class Solution:
    def solve(self, n):

        s = set()

        while n not in s:

            s.add(n)

            result = 0

            while n != 0:
                result += (n % 10) ** 2
                n //= 10

            n = result

            if n == 1:
                print("yes")

        print("no")
Solution().solve(32)