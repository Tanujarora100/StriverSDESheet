class Solution:
    def findClosestElements(self, arr, k, x):
        res = []
        left = 0
        right = len(arr) - 1

        while right - left > k - 1:
            # Shrink the window size from N to K
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1
        
        while left <= right:
            res.append(arr[left])
            left += 1
        
        return res