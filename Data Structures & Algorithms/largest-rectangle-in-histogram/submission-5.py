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

            

                        *
                    *   *
                    *   *
                    *   *       *
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
        heights+=[0]
        for i,h in enumerate(heights):
            if stack:
                pInd = i
                while stack and stack[-1][1]>=h:
                    pInd, pHeight = stack.pop()
                    maxArea = max(maxArea, pHeight*(i - pInd))
                stack.append((pInd,h))
            else:
                stack.append((i,h))
            maxArea = max(maxArea, h)
        for i in range(len(stack)):
            maxArea = max(maxArea, stack[i][1]*(len(heights) - stack[i][0]))
        return maxArea