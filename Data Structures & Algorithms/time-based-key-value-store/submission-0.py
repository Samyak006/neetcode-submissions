from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.Tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.Tmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l,r = 0,len(self.Tmap[key])-1
        val = self.Tmap[key]
        ret = ""
        while l<=r:
            m = (l+r)//2
            if val[m][0] > timestamp:
                r = m - 1
            else:
                ret = val[m][1]
                l = m + 1
        return ret

