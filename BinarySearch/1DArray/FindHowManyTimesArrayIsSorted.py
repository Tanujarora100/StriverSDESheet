class Solution:
    def findKRotation(self, arr, n):
        # Initialize start and end pointers
        start = 0
        end = n - 1

        # Perform binary search
        while start < end:
            mid = start + (end - start) // 2  # Calculate the middle index
            if arr[mid] > arr[end]:  # If the middle element is greater than the end element
                start = mid + 1  # Update start pointer
            else:
                end = mid  # Update end pointer

        return start  # Return the start pointer

