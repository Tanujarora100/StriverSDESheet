class Solution:
    def minDays(self, bloomDay, m, k):
        # Find the lowest and highest bloom days
        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1  # Set the default answer to -1

        # Check if it's possible to make m bouquets with k adjacent flowers with a given number of days
        def isPossible(mid):
            bouquets = 0
            flowers_collected = 0
            for value in bloomDay:
                if value <= mid:
                    flowers_collected += 1
                else:
                    flowers_collected = 0
                if flowers_collected == k:
                    bouquets += 1
                    flowers_collected = 0
            return bouquets >= m

        # Perform binary search to find the minimum number of days needed to make m bouquets with k adjacent flowers
        while low <= high:
            mid = low + (high - low) // 2
            if isPossible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

