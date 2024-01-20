class Solution:
    def isPossible(self, weights, days, mid):
        day = 1
        weight = 0
        for w in weights:
            if w > mid:
                return False
            if weight + w <= mid:
                weight += w
            else:
                day += 1
                weight = w
        return day <= days

    def shipWithinDays(self, weights, days):
        start = 0
        end = sum(weights)
        ans = -1
        while start <= end:
            mid = start + (end - start) // 2
            if self.isPossible(weights, days, mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans

