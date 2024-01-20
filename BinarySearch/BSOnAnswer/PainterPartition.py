class Solution:
    def isPossible(self, arr, n, m, mid):
        painter = 1
        board = 0
        for i in range(n):
            if arr[i] > mid:
                return False
            if board + arr[i] <= mid:
                board = board + arr[i]
            else:
                painter += 1
                if painter > m:
                    return False
                board = arr[i]
        return True

    def minTime(self, arr, n, k):
        end = sum(arr)
        start = 0
        ans = -1
        while start <= end:
            mid = start + (end - start) // 2
            if self.isPossible(arr, n, k, mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans


