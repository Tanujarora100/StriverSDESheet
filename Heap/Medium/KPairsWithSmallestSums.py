import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        max_heap = []
        heapq.heapify(max_heap)
        min_heap = []
        heapq.heapify(min_heap)
        visited = set()  # New set to track visited pairs
        for i in nums2:
            heapq.heappush(min_heap, (nums1[0] + i, 0, i))  # Store the sum, index of nums1, and value of nums2

        while min_heap and len(max_heap) < k:
            _, i, j = heapq.heappop(min_heap)
            pair = [nums1[i], j]
            max_heap.append(pair)
            visited.add(tuple(pair))

            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i + 1] + j, i + 1, j))

        return max_heap