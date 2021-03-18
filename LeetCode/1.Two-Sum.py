class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexList= []
        for i in range(0, len(nums)):
            try:
                if target-nums[i] in nums:
                    if i == nums.index(target-nums[i]):
                        continue
                    else:
                        indexList.append(i)
                        indexList.append(nums.index(target-nums[i]))
                    return indexList
            except:
                pass

        return indexList