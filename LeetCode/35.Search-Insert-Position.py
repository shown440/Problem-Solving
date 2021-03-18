class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # index = nums.index(target)
        nums_len = len(nums)
        for i in range(0,nums_len): 
            if target <= nums[i]:
                return i
            if i == (nums_len-1):
                return i+1
