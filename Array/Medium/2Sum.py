from typing import List




def two_sum(self, nums: List[int], target: int) -> List[int]:
    # Create an empty dictionary to store the numbers and their indices
    num_indices = {}
    # Iterate through the indices and values of the input list
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        # If the complement is in the dictionary, return the current index and the index of the complement
        if complement in num_indices:
            return [i, num_indices[complement]]
        # Store the current number and its index in the dictionary
        num_indices[num] = i