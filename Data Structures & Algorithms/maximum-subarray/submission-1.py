class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = 0
        curr = 0
        for i in nums:
            curr += i
            if curr < 0:
                curr = 0
            maxSum = max(maxSum, curr)
        if not maxSum: return max(nums)
        return maxSum 