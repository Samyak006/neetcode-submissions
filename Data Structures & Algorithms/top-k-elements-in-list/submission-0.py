from collections import Counter
import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        count = dict(Counter(nums))
        for i,j in count.items():
            hq.heappush(h,(-j,i))
        ret = []
        while k>0:
            ret.append(hq.heappop(h)[1])
            k-=1
        return ret