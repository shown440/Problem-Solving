class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            # print(nums[i-1],":", nums[i])
            # print(nums)
            if nums[i] == nums[i-1]: 
                nums.pop(i)
                i = i-1 
            i = i+1 
        return len(nums)
    
    