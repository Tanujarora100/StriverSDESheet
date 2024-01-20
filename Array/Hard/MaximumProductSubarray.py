class Solution:
    def maxProduct(self, nums):
        # Initialize prefix and suffix to 1
        prefix = 1
        suffix = 1

        # Get the length of the input array
        n = len(nums)

        # Initialize ans to the minimum possible value
        ans = float('-inf')

        # Iterate through the array
        for i in range(n):
            # If prefix becomes 0, reset it to 1
            if prefix == 0:
                prefix = 1
            # If suffix becomes 0, reset it to 1
            if suffix == 0:
                suffix = 1

            # Update prefix and suffix by multiplying with the current element
            prefix *= nums[i]
            suffix *= nums[n - i - 1]

            # Update ans with the maximum value among ans, prefix, and suffix
            ans = max(ans, max(prefix, suffix))

        # Return the maximum product
        return ans