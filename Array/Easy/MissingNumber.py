class Solution:
    def missingNumber(self, nums):
        # Initialize the result to 0
        res = 0
        # Get the length of the input array
        n = len(nums)
        
        # Loop through the input array and XOR the result with the array elements and their indices
        for i in range(n):
            res = res ^ nums[i] ^ i
        
        # XOR the result with the length of the input array and return the final result
        return res ^ n

