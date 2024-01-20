def insertion_sort(nums):
    """
    Insertion Sort Algorithm.

    Parameters:
    - nums: A list of numbers to be sorted in ascending order.

    Time Complexity:
    - Best Case: O(N) - Already sorted
    - Average Case: O(N^2)
    - Worst Case: O(N^2)

    Space Complexity:
    - Worst Case: O(1)
    """

    n = len(nums)

    for i in range(1, n):
        key = nums[i]  # Select the current element to be inserted
        j = i - 1

        # Move elements of nums[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key  # Place the selected element at its correct position

# Example Usage:
# nums = [64, 34, 25, 12, 22, 11, 90]
# insertion_sort(nums)
# print("Sorted array:", nums)
