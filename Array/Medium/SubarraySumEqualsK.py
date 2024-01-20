from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map=defaultdict(int)
        hash_map[0]=1
        tot=0
        count=0
        for i in range(len(nums)):
            tot+=nums[i]
            if tot-k in hash_map:
                count+=hash_map[tot-k]
            hash_map[tot]+=1
        return count

        