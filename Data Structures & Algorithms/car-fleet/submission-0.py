class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
            calculate the time required for individual cars to reach the destination
            maintain a stack for determining the car fleets
            return the final len of stack
        '''
        stack = []
        time = [(target-position[i])/speed[i] for i in range(len(speed))]
        sortedPosTime = list(sorted([(position[i],time[i]) for i in range(len(position))]))
        for _, t in sortedPosTime:
            if not stack:
                stack.append(t)
            else:
                while stack and stack[-1]<=t:
                    stack.pop()
                stack.append(t)
        return len(stack)
