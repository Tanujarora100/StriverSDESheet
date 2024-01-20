class Solution:
    def nextPermutation(self, nums):
        # Find the breakpoint of the array
        break_index = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                break_index = i
                break
        print(break_index)
        if break_index == -1:
            nums.reverse()  # Reverse the array in place
            #Reverse this array in place
            return 

        # Second Step => Get the closest greater element than the breakpoint number
        for i in range(len(nums)-1, break_index, -1):
            if nums[i] > nums[break_index]:
                # Swap the breakpoint element with the closest greater element
                nums[i], nums[break_index] = nums[break_index], nums[i]
                break

        # Third Step => Reverse the sub-array after the breakpoint to get the next permutation
        nums[break_index+1:] = reversed(nums[break_index+1:])