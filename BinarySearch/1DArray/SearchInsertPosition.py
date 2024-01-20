from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start+(end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid+1
            else:
                end = end-1
        return start