class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            # Find pivot element such that
            # elements smaller than pivot are on the left
            # elements greater than pivot are on the right
            pivot_index = self.partition(arr, low, high)

            # Recursively sort the sublists
            self.quickSort(arr, low, pivot_index)
            self.quickSort(arr, pivot_index + 1, high)

    def partition(self, arr, low, high):
        # Choose the rightmost element as the pivot
        pivot = arr[high]
        i = low - 1  # Index of smaller element

        # Traverse through the array and rearrange elements
        # such that elements smaller than pivot are on the left
        # and elements greater than pivot are on the right
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        # Swap the pivot element with the element at index i+1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        # Return the index of the pivot element
        return i + 1

# Example Usage:
# solution = Solution()
# arr = [64, 34, 25, 12, 22, 11, 90]
# solution.quickSort(arr, 0, len(arr) - 1)
# print("Sorted array:", arr)
