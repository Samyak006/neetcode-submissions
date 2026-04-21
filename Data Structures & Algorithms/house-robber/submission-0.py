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
        def maxProfit(i):
            if i<0: return 0
            if i in cache:
                return cache[i]
            curr = max(maxProfit(i-1),nums[i]+maxProfit(i-2))
            cache[i] = curr
            return curr
        return maxProfit(len(nums)-1)