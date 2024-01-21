from typing import List


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components=n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, root, child):
        root_parent = self.find(root)
        child_parent = self.find(child)
        if root_parent==child_parent:
            return False
        self.parent[child_parent]=root_parent
        self.components-=1
        return True

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        unionFind = DSU(n)
        for source, destination in connections:
            if source<destination:
                unionFind.union(source,destination)
        return unionFind.components-1
