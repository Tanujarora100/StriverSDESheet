class Solution:
    def longestConsecutive(self, nums):
        # If the input list is empty, return 0
        if not nums:
            return 0

        # Create a set from the input list to efficiently check for presence of a number
        num_set = set(nums)
        longest_streak = 0

        # Iterate through each unique number in the set
        for num in num_set:
            # If the current number minus 1 is not in the set, start a new streak
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Continue incrementing the current number and streak as long as the next number is in the set
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the longest streak with the current streak if it's longer
                longest_streak = max(longest_streak, current_streak)

        return longest_streak


