import heapq


class Solution:
    def findKthLargest(self, nums, k):
        pq=[]
        for i in nums:
            heapq.heappush(pq,i)
            if len(pq)==k+1:
                heapq.heappop(pq)
        return heapq.heappop(pq)