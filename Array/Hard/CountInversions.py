class Solution:
    # User function Template for python3

    # arr[]: Input Array
    # N : Size of the Array arr[]
    # Function to count inversions in the array.
    def inversionCount(self, arr, n):
        temp = [0] * n  # Temporary array for merging

        # Function to merge two halves and count inversions during the merge
        def merge_and_count(arr, temp, left, mid, right):
            i = left  # Index for the left subarray
            j = mid + 1  # Index for the right subarray
            k = left  # Index for the merged array
            count = 0  # Inversion count

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    # If arr[i] > arr[j], then arr[i] will be greater than all elements from arr[i] to arr[mid]
                    # So, increment the inversion count by the number of elements remaining in the left subarray
                    count += (mid - i + 1)
                    temp[k] = arr[j]
                    j += 1
                k += 1

            # Copy the remaining elements from the left subarray (if any)
            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1

            # Copy the remaining elements from the right subarray (if any)
            while j <= right:
                temp[k] = arr[j]
                j += 1
                k += 1

            # Copy the merged array back to the original array
            for i in range(left, right + 1):
                arr[i] = temp[i]

            return count

        # Function to recursively count inversions in the array using merge sort
        def merge_sort_and_count(arr, temp, left, right):
            count = 0

            if left < right:
                mid = (left + right) // 2

                # Recursively count inversions in the left and right subarrays
                count += merge_sort_and_count(arr, temp, left, mid)
                count += merge_sort_and_count(arr, temp, mid + 1, right)

                # Merge the two sorted subarrays and count inversions during the merge
                count += merge_and_count(arr, temp, left, mid, right)

            return count

        # Call the merge_sort_and_count function with the given array and return the result
        return merge_sort_and_count(arr, temp, 0, n - 1)