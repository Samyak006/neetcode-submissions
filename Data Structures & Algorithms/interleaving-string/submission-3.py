class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N, n, m = len(s3), len(s1), len(s2)
        if N == n+m:
            cache = {}
            def isValid(i,j,k):
                if i>=N:
                    return (j == n) and (k == m)
                if (j,k) in cache:
                    return cache[(j,k)]
                curr = False
                if j<n and s3[i] == s1[j]:
                    curr |=  isValid(i+1, j+1, k)
                if k<m and s3[i] == s2[k]:
                    curr |= isValid(i+1, j, k+1)
                cache[(j,k)] = curr    
                return curr
            return isValid(0,0,0)
        return False