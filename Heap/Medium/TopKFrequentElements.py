from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        # O(1) time
        if k == len(nums):
            return nums

        # 1. build hash map: element and how often it appears
        # O(N) time
        count = Counter(nums)

        # init heap 'the less frequent element first'
        heap = []
        
        # 2. keep k top frequent elements in the heap
        # O(N log k) < O(N log N) time
        for n in count:
            heapq.heappush(heap, (count[n], n))
            if len(heap) > k:
                heapq.heappop(heap)

        # 3. build an output array
        # O(k log k) time
        top = [0] * k
        for i in range(k - 1, -1, -1):
            top[i] = heapq.heappop(heap)[1]

        return top
