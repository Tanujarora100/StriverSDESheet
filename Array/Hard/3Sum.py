from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()  # Use a set to store unique triplets
        nums.sort()  # Sort the input list to make duplicate handling easier
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for i
                continue
            start = i + 1  # Set the start pointer for the current i
            end = len(nums) - 1  # Set the end pointer for the current i
            while start < end:
                if nums[i] + nums[start] + nums[end] == 0:  # Check if the triplet sums up to zero
                    ans.add((nums[i], nums[start], nums[end]))  # Add the triplet to the set
                    # Skip duplicates for start and end
                    while start < end and nums[start + 1] == nums[start]:  # Skip duplicate start values
                        start += 1
                    start += 1  # Move start pointer to the next unique value
                    while start < end and nums[end - 1] == nums[end]:  # Skip duplicate end values
                        end -= 1
                    end -= 1  # Move end pointer to the next unique value
                elif nums[i] + nums[start] + nums[end] < 0:  # If the sum is less than zero, move start pointer
                    start += 1
                else:  # If the sum is greater than zero, move end pointer
                    end -= 1
        return list(ans)  # Convert the set of triplets to a list and return
