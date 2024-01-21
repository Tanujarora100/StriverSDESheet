import heapq
import math
from typing import List


class Solution:
    def minStoneSum(self, nums: List[int], k: int) -> int:
        pq = []
        for i in range(len(nums)):
            heapq.heappush(pq, -nums[i])
        # score = 0
        while k > 0:
            element = -heapq.heappop(pq)
            # score += element
            temp_left_gifts = math.ceil(element / 2)
            heapq.heappush(pq, -temp_left_gifts)
            k -= 1
        return -sum(pq)