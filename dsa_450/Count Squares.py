class Solution:
    def search(self, nums: List[int], target: int) -> int:
        temp = nums[target]
        if len(nums) ==1:
            return -1
        new = nums[target:len(nums)] + nums[0:target]
        #print(new)
        if temp == new[target]:
            return temp
        else:
            return -1

