from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        # Create a frequency map using Counter
        freq_map = Counter(s)

        # Create a max heap (priority queue) based on frequency
        max_heap = [(-freq, char) for char, freq in freq_map.items()]
        heapq.heapify(max_heap)

        # Build the result string
        result = []
        while max_heap:
            # Pop the most frequent character from the max heap
            freq, char = heapq.heappop(max_heap)
            # Append the character to the result string, repeated by its frequency
            result.append(char * (-freq))

        # Join the characters in the result list to form the final string
        return ''.join(result)
