class Solution:
    def binarysearch(self, arr, n, k):
        start = 0
        end = n-1
        while start <= end:
            mid = start+(end-start)//2
            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                start = mid+1
            else:
                end = mid-1
        return -1