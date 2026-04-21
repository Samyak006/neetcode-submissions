class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevDict= {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            if target - nums[i] in prevDict and prevDict[target-nums[i]]!=i:
                return list(sorted([i,prevDict[target-nums[i]]])) 