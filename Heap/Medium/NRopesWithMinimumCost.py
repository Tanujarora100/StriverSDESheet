import heapq
 
 
def minCost(arr, n):
 
    # Create a priority queue out of the
    # given list
    heapq.heapify(arr)
 
    # Initialize result
    res = 0
 
    # While size of priority queue
    # is more than 1
    while(len(arr) > 1):
 
        # Extract shortest two ropes from arr
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
 
        # Connect the ropes: update result
        # and insert the new rope to arr
        res += first + second
        heapq.heappush(arr, first + second)
 
    return res