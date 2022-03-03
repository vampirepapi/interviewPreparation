class Solution:
    def countOdds(self, low: int, high: int) -> int:
        oddList=[]
        for x in range(low,high+1):
            if x%2!=0:
                oddList.append(x)
        return len(oddList)

p=Solution()
print(p.countOdds(3,7))

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        oddCount=0
        for x in range(low,high+1):
            if x%2!=0:
                oddCount+=1
        return oddCount

p=Solution()
print(p.countOdds(3,7))


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high-low
        # if any on the number high/low is odd
        if high %2 != 0 or low %2 != 0:
            return (diff // 2) +1
        else:
            return diff//2

p=Solution()
print(p.countOdds(3,7))