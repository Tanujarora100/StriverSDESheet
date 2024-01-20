from typing import List


class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        l = 0
        h = len(arr) - 1
        if h == 0:
            return 0  # base case, return 0 if array has only one element
        while h >= l:
            mid = l + (h - l) // 2
            if mid > 0 and mid < len(arr) - 1:
                if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                    return mid
                elif arr[mid] < arr[mid - 1]:
                    h = mid - 1
                else:
                    l = mid + 1
            elif mid == 0:
                if arr[mid] > arr[mid + 1]:
                    return 0
                else:
                    return 1
            elif mid == len(arr) - 1:
                if arr[mid] > arr[mid - 1]:
                    return len(arr) - 1
                else:
                    return len(arr) - 2
                    
        return 0
                

          
            