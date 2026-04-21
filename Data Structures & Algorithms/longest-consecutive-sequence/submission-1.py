class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ret = 0
        for i in nums:
            if i-1 not in numSet:
                k = i
                count = 0
                while k in numSet:
                    k+=1
                    count+=1
                ret = max(ret, count)
        return ret