from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals based on the start value
        intervals.sort()
        
        # Initialize an empty list to store the merged intervals
        merged = []
        
        # Append the first interval to the merged list
        merged.append(intervals[0])
        
        # Iterate through the remaining intervals
        for i in range(1, len(intervals)):
            # If the current interval overlaps with the last merged interval
            if intervals[i][0] <= merged[-1][1]:
                # Update the end value of the last merged interval if needed
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                # Add the current interval to the merged list
                merged.append(intervals[i])
        
        # Return the merged intervals
        return merged
