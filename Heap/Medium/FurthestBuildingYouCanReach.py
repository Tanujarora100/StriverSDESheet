# from heapimport heapq
import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq=[]
        for i in range(len(heights)-1):
            height_diff= heights[i+1]-heights[i]
            if height_diff>0:
                #Need a ladder to climb this
                heapq.heappush(pq,height_diff)
                if len(pq)>ladders:
                    bricks-=heapq.heappop(pq)
                if bricks<0:
                    return i
        return len(heights)-1