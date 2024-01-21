'''
Given an array a of integers of length n, find the nearest smaller number for every element such that the smaller element is on left side.If no small element present on the left print -1.

Example 1:

Input: n = 3
a = {1, 6, 2}
Output: -1 1 1
Explaination: There is no number at the 
left of 1. Smaller number than 6 and 2 is 1.
'''


class Solution:
    def leftSmaller(self, n, a):
        stack = []
        stack.append(-1)
        answer = []
        for i in range(n):
            while len(stack) > 1 and stack[-1] >= a[i]:
                stack.pop()
            answer.append(stack[-1])
            stack.append(a[i])
        # No need to reverse as we are making the list from the left and side itself
        return answer