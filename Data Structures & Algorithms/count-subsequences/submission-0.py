class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def numDist(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            a = numDist(i+1,j)
            if s[i] == t[j]:
                a += numDist(i+1,j+1)
            cache[(i,j)] = a
            return a
        return numDist(0,0)