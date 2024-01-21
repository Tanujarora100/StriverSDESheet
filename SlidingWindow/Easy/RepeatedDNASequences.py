from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        hash_map = {}
        i = 0
        j = 0
        k = 10
        tmp = ""
        while j < len(s):
            tmp += s[j]
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                hash_map[tmp] = hash_map.get(tmp, 0) + 1
                tmp = tmp[1:]
                j += 1
                i += 1

        for key, value in hash_map.items():
            if value > 1:
                ans.append(key)

        return ans