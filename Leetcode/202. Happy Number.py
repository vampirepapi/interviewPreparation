class Solution:
    def isHappy(self, n: int) -> bool:

        def sqsum(num):
            res = 0
            while num>0:
                r = num%10
                res += (r*r)
                num = num//10

            return res

        seen = set()
        while sqsum(n) not in seen :
            sum = sqsum(n)

            if sum == 1:
                return True
            else:
                seen.add(sum)
                n = sum
        return False

# p=Solution()
# print(p.isHappy(19))
            
        