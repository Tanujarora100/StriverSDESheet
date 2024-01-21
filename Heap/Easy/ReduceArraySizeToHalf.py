from collections import Counter
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        items = sorted(counts.items(), key = lambda x: x[-1], reverse = True)
    
        target = len(arr) / 2
        ans = 0
    
        for key, val in items:
            ans += 1
            target -= val
            if target <= 0:
                return ans
    
        return ans