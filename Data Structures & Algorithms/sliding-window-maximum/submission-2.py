import heapq as hq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sp = 0
        h = []
        n = len(nums)
        c = 0
        ret = []
        init = True
        for i in range(n):
            if c<k-1 and init:
                hq.heappush(h,(-nums[i],i))
                c+=1
                if c == k-1:
                    init = True
            else:
                hq.heappush(h,(-nums[i],i))
                val,ind = hq.heappop(h)
                if ind<sp:
                    while ind<sp and h:
                        val,ind = hq.heappop(h)
                hq.heappush(h,(val,ind))
                ret.append(-val)
                sp+=1
        return ret