class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = float("inf")
        maxProfit = 0
        for i in prices:
            if curr>i:
                curr = i
            else:
                maxProfit = max(maxProfit,i - curr)
        return maxProfit