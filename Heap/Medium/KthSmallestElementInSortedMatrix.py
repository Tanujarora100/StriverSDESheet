import heapq
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Check if the matrix is empty
        if not matrix or not matrix[0]:
            return -1  # Return -1 if the matrix is empty

        # Create a min heap to store the negative values of the matrix elements
        heap = []

        # Iterate through each element in the matrix
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                # Get the negative value of the current matrix element
                nextVal = -matrix[row][col]

                # If the heap has less than k elements, push the next value to the heap
                if len(heap) < k:
                    heapq.heappush(heap, nextVal)
                # If the next value is greater than the smallest value in the heap, replace the smallest value with the next value
                elif nextVal > heap[0]:
                    heapq.heappushpop(heap, nextVal)

        # Return the kth smallest element by taking the negative of the smallest value in the heap
        return -heap[0]
