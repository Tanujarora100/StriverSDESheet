import heapq

class SeatManager:

    def __init__(self, n: int):
        self.pq = list(range(1, n+1))
        heapq.heapify(self.pq)

    def reserve(self) -> int:
        if self.pq:
            return heapq.heappop(self.pq)
        return -1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.pq, seatNumber)
