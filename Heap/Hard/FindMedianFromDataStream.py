import heapq

class MedianFinder:
    def __init__(self):
        # Max heap for the smaller half of numbers
        self.maxHeap = []
        # Min heap for the larger half of numbers
        self.minHeap = []

    def addNum(self, num: int) -> None:
        # If maxHeap is empty or the number is less than or equal to the largest in maxHeap
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        # Balancing heaps to ensure the size difference is at most 1
        self._balancingHeaps()

    def findMedian(self) -> float:
        # If maxHeap has more elements, return the largest element
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        # If minHeap has more elements, return the smallest element
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        # If both heaps have equal size, return the average of the largest from maxHeap and smallest from minHeap
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0

    def _balancingHeaps(self) -> None:
        # If the size difference is greater than 1, move the root of the larger heap to the smaller heap
        if len(self.maxHeap) - len(self.minHeap) > 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) - len(self.maxHeap) > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
