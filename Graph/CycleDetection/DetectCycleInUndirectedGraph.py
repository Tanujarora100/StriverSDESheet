from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = set()
        parent_dictionary = {}
        queue = deque()
    
        for i in range(V):
            if i not in visited:
                if self.bfs(visited, parent_dictionary, i, queue, adj):
                    return True
    
        return False
        
    def bfs(self, visited, parent_dict, i, queue, adj):
        queue.append(i)
        visited.add(i)
        parent_dict[i] = -1
    
        while queue:
            curr_node = queue.popleft()
    
            for neighbor in adj[curr_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent_dict[neighbor] = curr_node
                    
                elif neighbor in visited and  parent_dict[curr_node] != neighbor:
                    return True
    
        return False








