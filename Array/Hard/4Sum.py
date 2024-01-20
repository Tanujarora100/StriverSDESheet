class Solution:
    def fourSum(self, nums, target):
        # Initialize the answer list
        ans = []
        
        # Sort the input array
        nums.sort()

        n = len(nums)
        
        # Loop through the array to find the first number in the quadruplet
        for i in range(n - 3):
            # Skip duplicate numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Loop through the array to find the second number in the quadruplet
            for j in range(i + 1, n - 2):
                # Skip duplicate numbers
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Initialize pointers for the third and fourth numbers in the quadruplet
                start, end = j + 1, n - 1
                
                # Use two pointers approach to find the third and fourth numbers
                while start < end:
                    total = nums[i] + nums[j] + nums[start] + nums[end]
                    if total < target:
                        start += 1
                    elif total > target:
                        end -= 1
                    else:
                        # Add the quadruplet to the answer list
                        ans.append([nums[i], nums[j], nums[start], nums[end]])
                        
                        # Skip duplicate numbers
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1
                        
                        # Move the pointers
                        start, end = start + 1, end - 1
        
        return ans
