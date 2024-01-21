# https://leetcode.com/problems/maximum-product-after-k-increments/description/

import heapq
from typing import List


class Solution:
    def maximumProduct(self, nums, k):
        MOD = int(1e9) + 7
        pq = []
        for num in nums:
            heapq.heappush(pq, num)

        while k > 0:
            smallest_number = heapq.heappop(pq)
            smallest_number += 1
            heapq.heappush(pq, smallest_number)
            k -= 1

        result = 1
        while pq:
            result = (result * heapq.heappop(pq)) % MOD

        return int(result)


