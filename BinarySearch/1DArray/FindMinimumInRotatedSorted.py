class Solution:
    @staticmethod
    def findMin(arr):
        low, high = 0, len(arr) - 1
        ans = float('inf')

        while low <= high:
            mid = (low + high) // 2

            # if left part is sorted:
            if arr[low] <= arr[mid]:
                # keep the minimum:
                ans = min(ans, arr[low])

                # Eliminate left half:
                low = mid + 1
            else:  # if right part is sorted:
                # keep the minimum:
                ans = min(ans, arr[mid])

                # Eliminate right half:
                high = mid - 1

        return ans


