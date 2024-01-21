class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1  # Index for nums1
        j = n - 1  # Index for nums2
        ptr = m + n - 1  # Index for the result array

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[ptr] = nums1[i]
                i -= 1
            else:
                nums1[ptr] = nums2[j]
                j -= 1
            ptr -= 1

        # If there are remaining elements in nums2, copy them to nums1
        while j >= 0:
            nums1[ptr] = nums2[j]
            j -= 1
            ptr -= 1
