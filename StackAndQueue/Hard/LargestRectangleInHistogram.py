from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftSmaller= self.leftSmallerElements(heights)
        rightSmaller= self.rightSmallerElements(heights)
        area= float('-inf')
        n= len(heights)
        for i in range(n):
            l = heights[i]
            if rightSmaller[i] == -1:
                rightSmaller[i] = n
            b = rightSmaller[i] - leftSmaller[i] - 1
            newArea = l * b
            area = max(area, newArea)
        return area
            


    def leftSmallerElements(self, heights):
        stack = []
        stack.append(-1)
        result = [0] * len(heights)
        for i in range(len(heights)):
            curr = heights[i]
            while stack[-1] != -1 and heights[stack[-1]] >= curr:
                stack.pop()
            result[i] = stack[-1]
            stack.append(i)
        return result
    
    def rightSmallerElements(self, heights):
        stack = []
        stack.append(-1)
        result = [0] * len(heights)
        for i in range(len(heights)-1, -1, -1):
            curr = heights[i]
            while stack[-1] != -1 and heights[stack[-1]] >= curr:
                stack.pop()
            result[i] = stack[-1]
            stack.append(i)
        return result