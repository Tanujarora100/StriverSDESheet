import math

class Solution:
    def smallestDivisor(self, nums, threshold):
        start = 1
        end = sum(nums)
        ans = -1
        while start <= end:
            mid = start + (end - start) // 2
            if self.solve(mid, nums, threshold):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans

    def solve(self, mid, nums, threshold):
        curr_sum=0
        for num in nums:
           curr_sum+=math.ceil(num/mid)
        return curr_sum<=threshold