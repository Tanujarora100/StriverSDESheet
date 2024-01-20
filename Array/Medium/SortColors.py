class Solution:
    def sortColors(self, nums):
        mid = 0
        high = len(nums) - 1
        low = 0
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Example Usage:
# solution = Solution()
# nums = [2, 0, 2, 1, 1, 0]
# solution.sortColors(nums)
# print(nums)
