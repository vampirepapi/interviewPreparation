class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        while n:
            n=n&(n-1)
            c+=1
        return c

c=Solution()
print(c.Solution(00000000000000000000000000001011))