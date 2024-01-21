def wiggle_sort(nums):
    for i in range(1, len(nums)):
        if i % 2 == 0 and nums[i] > nums[i - 1]:
            swap(i, i - 1, nums)
        elif i % 2 != 0 and nums[i] < nums[i - 1]:
            swap(i, i - 1, nums)

def swap(i, j, nums):
    nums[i], nums[j] = nums[j], nums[i]

# Example Usage:
nums = [3, 5, 2, 1, 6, 4]
wiggle_sort(nums)
print(nums)
