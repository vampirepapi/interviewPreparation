class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        n=set()
        for i in s:
            n.add(s.count(i))
        return len(n)==1 