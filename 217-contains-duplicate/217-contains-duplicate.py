class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        noDup=set(nums)
        if len(noDup) != len(nums):
            return True;
        return False;