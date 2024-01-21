from collections import Counter
from heapq import heapify, heappop, heappush
from queue import PriorityQueue

class Solution:
    def leastInterval(self, tasks, n):
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapify(max_heap)
        
        waiting_queue = PriorityQueue()
        time = 0

        while max_heap or not waiting_queue.empty():
            time += 1

            if max_heap:
                count = -heappop(max_heap) - 1
                waiting_queue.put((-count, time + n) if count != 0 else None)

            if not waiting_queue.empty() and waiting_queue.queue[0][1] == time:
                heappush(max_heap, -waiting_queue.get()[0])

        return time

# Example usage:
solution = Solution()
tasks = ['A', 'A', 'A', 'B', 'B', 'B']
n = 2
result = solution.leastInterval(tasks, n)
print(result)
