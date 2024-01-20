class Solution:
    def check(self, nums):
        # Initialize count to keep track of the number of times the condition is met
        count = 0
        # Get the length of the input list
        n = len(nums)
        
        # Iterate through the input list
        for i in range(n):
            # Check if the current number is greater than the next number in a circular manner
            if nums[i] > nums[(i + 1) % n]:
                # Increment count if the condition is met
                count += 1
        
        # Return True if the count is less than or equal to 1, else return False
        return count <= 1


