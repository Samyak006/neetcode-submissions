import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isRateEnough(k):
            hrs = 0
            for p in piles:
                hrs+=math.ceil(p/k)
            return hrs<=h
        l,r = 1, max(piles)
        ret = float("inf")
        while l<=r:
            m = (l+r)//2
            if isRateEnough(m):
                ret = m
                r = m - 1
            else:
                l = m + 1
        return ret