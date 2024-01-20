
from collections import defaultdict
class Solution:
    def maxLen(self, n, arr):
        hash_map=defaultdict(int)
        hash_map={0:-1}
        curr_ans=0
        prefix_sum=0
        ans=0
        for i in range(n):
            prefix_sum+=arr[i]
            if prefix_sum in hash_map:
                curr_ans= i-hash_map[prefix_sum]
                ans= max(ans,curr_ans)
            else:
                hash_map[prefix_sum]=i
        return ans
            
