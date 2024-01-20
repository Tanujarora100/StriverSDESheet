class Solution:

    def count(self, arr, n, x):
        def first_occurence(nums, target, first_occurence):
            start = 0
            end = len(nums)-1
            while start <= end:
                mid = start+(end-start)//2
                if nums[mid] > target:
                    end = mid-1
                elif nums[mid] < target:
                    start = mid+1
                else:
                    first_occurence = mid
                    end = mid-1
            return first_occurence

        def last_occurence(nums, target, last_occurence):
            start = 0
            end = len(nums)-1
            while start <= end:
                mid = start+(end-start)//2
                if nums[mid] < target:
                    start = mid+1
                elif nums[mid] > target:
                    end = mid-1
                else:
                    last_occurence = mid
                    start = mid+1
            return last_occurence
        left_occurence = first_occurence(arr, x, -1)
        right_occurence = last_occurence(arr, x, -1)
        if left_occurence == -1:
            return 0
        return right_occurence-left_occurence+1