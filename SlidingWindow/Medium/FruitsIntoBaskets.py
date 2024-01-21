import collections
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        k=2
        left=0
        right=0
        max_ans=0
        hash_map=collections.defaultdict(int)
        while right<len(fruits):
            hash_map[fruits[right]]+=1

            if len(hash_map)<=k:
                max_ans= max(max_ans,right-left+1)
                right=right+1
            else:
                # while len(hash_map)>k:
                hash_map[fruits[left]]-=1
                if hash_map[fruits[left]]==0:
                    del hash_map[fruits[left]]
                left=left+1
                right=right+1
        return max_ans