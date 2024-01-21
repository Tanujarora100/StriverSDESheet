from typing import List


# 1762-Buildings with Ocean View
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        stack.append(-1)
        for i in range(len(heights)):
            while len(stack) > 1 and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)
        stack.remove(-1)
        return stack
        # This is based on next greater element
        # We will put the elements in the stack only if they are greater than the top
    # Here we need to give indexes so we are smartly storing the indexes and then returning them
    # Otherwise we can store pairs also.