def heapify(nums, n, i):
    """
    Heapify the subtree rooted at index i.

    Parameters:
    - nums: A list of numbers.
    - n: Size of the heap.
    - i: Index of the root of the subtree.

    Time Complexity: O(log N)
    """

    largest = i  # Initialize the root as the largest
    left_child = 2 * i + 1  # Left child
    right_child = 2 * i + 2  # Right child

    # Check if the left child is larger than the root
    if left_child < n and nums[left_child] > nums[largest]:
        largest = left_child

    # Check if the right child is larger than the largest so far
    if right_child < n and nums[right_child] > nums[largest]:
        largest = right_child

    # Swap the root if needed and recursively heapify the affected subtree
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)


def heap_sort(nums):
    """
    Heap Sort Algorithm.

    Parameters:
    - nums: A list of numbers to be sorted in ascending order.

    Time Complexity:
    - Best Case: O(N log N)
    - Average Case: O(N log N)
    - Worst Case: O(N log N)

    Space Complexity:
    - Worst Case: O(1)
    """

    n = len(nums)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]  # Swap
        heapify(nums, i, 0)  # Heapify the reduced heap

# Example Usage:
# nums = [64, 34, 25, 12, 22, 11, 90]
# heap_sort(nums)
# print("Sorted array:", nums)
