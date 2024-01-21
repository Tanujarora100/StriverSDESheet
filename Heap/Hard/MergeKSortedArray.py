import heapq

class Solution:
    class TripletNode:
        def __init__(self, data, array_position, value_position):
            self.data = data
            self.array_position = array_position
            self.value_position = value_position

    def merge_k_arrays(self, arr, k):
        pq = []
        heapq.heapify(pq)
        ans_list = []

        for i in range(k):
            heapq.heappush(pq, self.TripletNode(arr[i][0], i, 0))

        while pq:
            min_element = heapq.heappop(pq)
            ans_list.append(min_element.data)
            next_index = min_element.value_position + 1

            if next_index < len(arr[min_element.array_position]):
                heapq.heappush(pq, self.TripletNode(arr[min_element.array_position][next_index], min_element.array_position, next_index))

        return ans_list

# Example usage:
solution = Solution()
arrays = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [0, 9, 10, 11]
]
k = len(arrays)
result = solution.merge_k_arrays(arrays, k)
print(result)
