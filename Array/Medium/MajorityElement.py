from typing import List


class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        # Initialize candidate and vote count
        candidate = arr[0]
        vote = 0
        # Iterate through the array
        for i in range(len(arr)):
            # If current element is the candidate, increase the vote count
            if arr[i] == candidate:
                vote += 1
            else:
                # If current element is not the candidate, decrease the vote count
                vote -= 1
            # If vote count becomes zero or negative, update candidate and reset vote count to 1
            if vote <= 0:
                vote = 1
                candidate = arr[i]
        # Return the majority element
        return candidate
