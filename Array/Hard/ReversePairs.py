from typing import List


class Solution:


    def reversePairs(self, nums: List[int]) -> int:
        # Initialize count of reverse pairs
        cnt = 0

        # Define merge function to merge two sorted lists and count reverse pairs
        def merge(left, right):
            nonlocal cnt
            i = j = 0
            merged = []
            while i < len(left) and j < len(right):
                # If condition for reverse pair
                if left[i] <= 2*right[j]:
                    i += 1
                else:
                    cnt += len(left) - i
                    j += 1

            # Sort and return the merged list
            return sorted(left + right)

        # Define mergeSort function to recursively split and merge the list
        def mergeSort(A):
            # Base case: if list has 1 or 0 elements, return the list
            if len(A) <= 1:
                return A
            # Recursively split and merge the list
            return merge(mergeSort(A[:(len(A) + 1) // 2]), mergeSort(A[(len(A) + 1) // 2:]))

        # Call the mergeSort function to sort the input list and update reverse pair count
        mergeSort(nums)
        # Return the count of reverse pairs
        return cnt
