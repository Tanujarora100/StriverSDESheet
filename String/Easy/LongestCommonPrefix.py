from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort the array and then compare the first and last string
        strs.sort()
        str_start = strs[0]
        str_last = strs[-1]
        count = 0
        for i in range(len(str_start)):
            if (str_start[i] != str_last[i]):
                break
            else:
                count += 1
        return "" if count==0 else str_start[0:count]