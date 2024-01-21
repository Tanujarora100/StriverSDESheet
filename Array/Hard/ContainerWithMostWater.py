from typing import List


class Solution:
    def maxArea(self, arr: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(arr) - 1
        while left < right:
            area = min(arr[left], arr[right]) * (right - left)
            max_area = max(max_area, area)
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        return max_area