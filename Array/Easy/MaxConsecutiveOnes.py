from typing import List


def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    # Initialize count and max_count to 0
    count = 0
    max_count = 0
    
    # Iterate through the nums list
    for num in nums:
        # If the current number is 1, increment count
        if num == 1:
            count += 1
        else:
            # Update max_count if count is greater than the current max_count
            max_count = max(max_count, count)
            # Reset count to 0
            count = 0
            
    # Return the maximum of max_count and count
    return max(max_count, count)
       
        
        