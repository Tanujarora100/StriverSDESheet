from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = 10**9
        ans = -1
        while start <= end:
            mid = start + (end - start) // 2
            if self.is_possible(piles, h, mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans
   
    def is_possible(self,arr, h, mid):
        hours = 0
        for it in arr:
            hours += it // mid
            # print(hours)
            if it % mid != 0:
                hours += 1
        return hours <= h
