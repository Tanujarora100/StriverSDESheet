import heapq

class Solution:
    # Function to return the sorted array.
    def nearlySorted(self, arr, num, k):
        min_heap = []

        for it in arr:
            heapq.heappush(min_heap, it)
            if len(min_heap) > k:
                num = heapq.heappop(min_heap)

        while min_heap:
            num = heapq.heappop(min_heap)

        return arr
