class Solution:
    def rearrangeArray(self, nums):
        # Edge cases
        if len(nums) < 2:
            return nums

        posi = 0
        negi = 1
        new_array = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                new_array[posi] = nums[i]
                posi += 2
            else:
                new_array[negi] = nums[i]
                negi += 2

        return new_array

