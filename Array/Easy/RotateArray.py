from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0:
            return None
        
        # Approach- Make a copy array of the same size
        # Add the elements of ith index at i+k index in the copy array.
        # Make sure that i+k index is % of the size of the array to make the addition circular.
        # At the end copy the copy_array to the original array

        copy_array=[-1]*len(nums)
        for i in range(len(nums)):
            copy_array[(i + k) % len(nums)] = nums[i]
        
        # Copy the copy_array to the original array

        for i in range(len(nums)):
            nums[i]=copy_array[i]
        # Time Complexity-O(N)
        # Space Complexity-O(N)
    
    def rotate_optimized(self,nums, k):
        if len(nums) == 0:
            return nums
        # Approach
        # First reverse the whole array from 0 - n-1
        # Reverse the Elements from 0 to k-1
        # Reverse from k to end at the end of the array

        # Make sure that you take modulo of k before reversing otherwise it will go out of bounds.
        n= len(nums)
        k=k%n
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        

    def reverse(self,nums, start, end):
        left = start
        right = end
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    