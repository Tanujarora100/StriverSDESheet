from collections import deque
from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return 0
        time = [0] * n
        edge = [[] for _ in range(n)]
        
        for i in range(n):
            if manager[i] != -1:
                edge[manager[i]].append(i)
        
        max_time = 0
        q = deque([headID])
        
        while q:
            curr = q.popleft()
            for sub in edge[curr]:
                time[sub] = time[curr] + informTime[curr]
                max_time = max(max_time, time[sub])
                q.append(sub)
        
        return max_time
