class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        preHeights = [0]*n
        postHeights = [0]*n
        for i in range(1,n):
            preHeights[i] = max(preHeights[i-1],height[i-1])
        for i in range(n-2, -1, -1):
            postHeights[i] = max(postHeights[i+1],height[i+1])
        maxTrapped = 0
        for i in range(n):
            maxTrapped += (max(0,min(preHeights[i],postHeights[i])-height[i]))
        return maxTrapped