class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
            *       *
            *       *
            *       *
            *       *           *
            *       *           *
            *       *   *   *   *
            *   *   *   *   *   *


            stack, 
            append 0 to the heights array
            initialize a maxArea variable to keep track of max Height
            iterate through the heights array:
            maxArea = max(maxArea, current height)
            if the top height is less than equal to curr height 
                maxArea = max(maxArea, curHeight * (top Index - currIndex)) and replace the top with curr height and maintain the previous index
            if the top height is greater than curr height add the height and index
        '''
        maxArea = 0
        stack = []
        heights.append(0)
        for i in range(len(heights)):
            maxArea = max(maxArea, heights[i])
            if not stack:
                stack.append((heights[i],i))
            else:
                start = i
                while stack and stack[-1][0]>heights[i]:
                    h,ind = stack.pop()
                    maxArea = max(maxArea, h*(i-ind))
                    start = ind
                stack.append((heights[i],start))
        for i in range(len(stack)-1):
            maxArea = max(maxArea, stack[i][0]*(len(heights)-stack[i][1]))
        return maxArea