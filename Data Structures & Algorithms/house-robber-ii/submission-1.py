class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            maxProfit(i) -> maximum profit obtained after robbing 0 to ith house. 
            return maxProfit(n)
            maxProfit(i) - > {
                0   if i < 0 
                max(maxProfit(i+1), nums[i]+maxProfit(i+2)) else
            }
        '''
        cache = {} 
        n = len(nums)        
        def maxProfit(i, isFirst):
            if isFirst and i == n-1:
                return 0
            if i>=n: return 0
            if (i, isFirst) in cache:
                return cache[(i,isFirst)]
            curr = max(maxProfit(i+1, isFirst),nums[i]+maxProfit(i+2,isFirst or i == 0))
            cache[(i,isFirst)] = curr
            return curr
        if len(nums) == 1:
            return nums[0]
        return max(maxProfit(1, False),maxProfit(0, True))