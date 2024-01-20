def bubble_sort(nums):
    n = len(nums)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                # Swap elements if they are in the wrong order
                nums[i], nums[j] = nums[j], nums[i]

# Example Usage:
# nums = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(nums)
# print("Sorted array:", nums)
