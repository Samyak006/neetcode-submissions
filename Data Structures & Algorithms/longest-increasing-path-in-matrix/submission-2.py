class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
            args: matrix
            return length of longest increasing path in matrix
            TC - O(N^2)
            Algo:
                Brute:
                    dfs from all possible (i,j) in the matrix
                    TC - O(N^3)
                Optimization: 
                    add a cache for all the states(i,j) and retrieve the maxLen to that point -> O(n^2)
        """
        m,n = len(matrix), len(matrix[0])
        def invalid(i,j):
            if i<0 or i>m-1 or j<0 or j>n-1:
                return True
            return False
        dirs = [(0,1), (1,0), (-1,0), (0,-1)] # up, right, left, down
        cache = {}
        def dfs(i,j):
            if (i,j) in cache: 
                return cache[(i,j)]
            curr = 0
            for x,y in dirs:
                if not invalid(i+x,j+y) and  matrix[i][j] < matrix[i+x][j+y]:
                    curr = max(curr, 1+dfs(i+x, j+y))
            cache[(i,j)] = curr
            return curr
        ret = 0
        for i in range(m):
            for j in range(n):
                print(i,j)
                ret = max(ret, 1+ dfs(i,j))
        return ret
            
            
