from typing import List


class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        # self.rank = [0] *( n+1)
        self.ans=[]

    def find(self, x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x==root_y:
            self.ans.append(x)
            self.ans.append(y)
            
        self.parent[root_y]=root_x

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionFind= DSU(len(edges))
        for u, v in edges:
            if u<v:
                unionFind.union(u,v)
            if len(unionFind.ans)>0:
                return unionFind.ans
        return []
            