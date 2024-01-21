import heapq

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        maxHeap = [-a, -b, -c]
        heapq.heapify(maxHeap)

        maxScore = 0
        while len(maxHeap) >= 2:
            maxElement = -heapq.heappop(maxHeap)
            secondMax = -heapq.heappop(maxHeap)

            maxScore += 1
            maxElement -= 1
            secondMax -= 1

            if maxElement != 0:
                heapq.heappush(maxHeap, -maxElement)
            if secondMax != 0:
                heapq.heappush(maxHeap, -secondMax)

        return maxScore
