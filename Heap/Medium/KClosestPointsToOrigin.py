import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Initialize an empty list to store the k closest points
        ans = []
        # Initialize an empty priority queue
        pq = []
        # Iterate through each point in the input list
        for (x, y) in points:
            # If the priority queue has k points, replace the point with the largest distance
            if len(pq) == k:
                heapq.heappushpop(pq, (-(x*x + y*y), x, y))
            # Otherwise, push the point into the priority queue
            else:
                heapq.heappush(pq, (-(x*x + y*y), x, y))
        # Pop each point from the priority queue and append it to the ans list
        while pq:
            _, xCord, yCord = heapq.heappop(pq)
            ans.append([xCord, yCord])
        # Return the k closest points
        return ans
