class Solution:
    
    def buildParentMap(self, node, parent, parentMap):
        if node is None:
            return
        parentMap[node] = parent
        self.buildParentMap(node.left, node, parentMap)
        self.buildParentMap(node.right, node, parentMap)
        
        
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # node: parent
        parentMap = {}
        
        # DFS to build the map that maps a node to its parent.
        self.buildParentMap(root, None, parentMap)
       
        # keep the records, since the graph is all connected
        visited = set()
        # results
        ans = []
       
        # Again, DFS to retrieve the nodes within the given distance
        #  this time with the help of the parentMap.
        # Starting from the target node
        def dfs(node, distance):
            if node is None or node in visited:
                return
            
            visited.add(node)
            if distance>K:
                return
            if distance == K:
                ans.append(node.val)
            elif distance < K:
                dfs(node.left, distance+1)
                dfs(node.right, distance+1)
                dfs(parentMap[node], distance+1)
            # else exceed the scope, no need to explore further
        
        dfs(target, 0)
        
        return ans