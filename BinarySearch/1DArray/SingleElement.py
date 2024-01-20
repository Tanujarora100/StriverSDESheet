from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans = ans ^ nums[i]
        return ans
    # Time Complexity-O(N)
    # Space Complexity-O(1)

    def singleNonDuplicate(self, nums: List[int]) -> int:
        dups = {}
        for i in range(len(nums)):
            if nums[i] not in dups:
                dups[nums[i]] = 1
            else:
                dups[nums[i]] += 1
        single_element = 0
        for keys, values in dups.items():
            if values == 1:
                single_element = keys
        return single_element
    # Time Complexity-O(N)
    # Space Complexity-O(N)

    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        while start < end:
            mid = start+(end-start)//2
            if mid % 2 == 1:
                mid = mid-1
            if nums[mid] == nums[mid+1]:
                start = start+2
            else:
                end = mid
        return nums[start]