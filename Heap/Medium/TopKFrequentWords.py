from collections import Counter

import heapq
from typing import List

class Solution:
    def topKFrequent(self, words, k):
        # Count the frequency of each word
        word_counts = Counter(words)

        # Create a min heap to store the k most frequent words
        min_heap = []
        for word, count in word_counts.items():
            # Push the word and its count into the min heap
            heapq.heappush(min_heap, (count, word))
            # If the heap size exceeds k, remove the least frequent word
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Sort the remaining words based on frequency and lexicographical order
        #Sorting on two things, if the count is more then it fires the first expression
        # If the count is same then the second one would be fired
        result = [word for _, word in sorted(min_heap, key=lambda x: (-x[0], x[1]))]
        return result
