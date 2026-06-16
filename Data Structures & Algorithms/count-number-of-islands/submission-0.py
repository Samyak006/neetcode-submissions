class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        '''
        def invalid(i,j):
            if i<0 or i>=len(grid) or j <0 or j>=len(grid[0]):
                return True
            return False
        
        dirs = [(0,1),(-1,0),(1,0),(0,-1)]
        
        ones = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ones.append((i,j))
        
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        ret = 0
        for i,j in ones:
            if not visited[i][j]: 
                q = [(i,j)]
                while q:
                    i,j = q.pop(0)
                    visited[i][j] = True
                    for x,y in dirs:
                        if not invalid(i+x,j+y) and not visited[i+x][j+y] and grid[i+x][j+y] == "1":
                            q.append((i+x,j+y))
                ret+=1
        return ret