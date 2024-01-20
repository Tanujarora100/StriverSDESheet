class Solution:
    def removeDuplicates(self, nums):
        # Initialize the index where unique elements will be inserted
        insert_index = 1

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Skip to the next index if a duplicate element is found
            if nums[i - 1] != nums[i]:
                # Store the unique element at insert_index and increment insert_index by 1
                nums[insert_index] = nums[i]
                insert_index += 1

        return insert_index

