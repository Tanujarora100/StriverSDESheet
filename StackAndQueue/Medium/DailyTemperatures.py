from typing import List


class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        stack = []
        ans = []
        stack.append([0, 0])
        for i in range(len(arr) - 1, -1, -1):
            curr_element = arr[i]
            while len(stack) > 0 and stack[-1][0] <= curr_element:
                stack.pop()
            ans.append(stack[-1][1] - i if stack else 0)
            stack.append([arr[i], i])
        return list(reversed(ans))