from collections import defaultdict
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, s: List[int]) -> int:
        hash_map = defaultdict(int)
        i = 0
        j = 0
        ans = 0
        while j < len(s):
            hash_map[s[j]] += 1
            if hash_map[0] <= 1:
                ans = max(ans, j-i+1)
                j = j+1
            else:
                while hash_map[0] > 1:
                    hash_map[s[i]] -= 1
                    if hash_map[s[i]] == 0:
                        del hash_map[s[i]]
                    i = i+1
                j = j+1
        return ans