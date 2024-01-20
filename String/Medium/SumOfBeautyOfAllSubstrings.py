import itertools


class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0  # Initialize the answer variable
        for i in range(len(s)):  # Loop through each character in the string
            bucket = [0] * 26  # Create a bucket to store the frequency of each letter
            for j in range(i, len(s)):  # Loop through the string from the current position to the end
                bucket[ord(s[j]) - ord('a')] += 1  # Increment the count of the corresponding letter in the bucket
    def beauty(self, bucket):
        # Initialize min_val and max_val to positive and negative infinity
        min_val, max_val = float('inf'), float('-inf')
        
        # Iterate through the range of 26 (the number of letters in the alphabet)
        for i in range(26):
            # If the count for the current letter is 0, skip to the next iteration
            if bucket[i] == 0:
                continue
            
            # Update min_val and max_val based on the current letter count
            min_val = min(min_val, bucket[i])
            max_val = max(max_val, bucket[i])
        
        # Return the difference between the maximum and minimum letter counts
        return max_val - min_val
            
