from collections import deque

from Tree.BinaryTree.Easy.IterativeInorder import TreeNode


class Codec:

    def serialize(self, root):
        ans = []
        queue = [root]
        for node in queue: 
            if node: ans.append(node.val)
            else: ans.append('N')
            if node: 
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(map(str, ans))

    def deserialize(self, data):
        root = parent = None 
        queue = deque()
        for x in data.split(','): 
            if x == 'N': node = None
            else: node = TreeNode(int(x))
            if not root: root = node 
            elif parent: 
                parent.right = node 
                parent = None 
            else: 
                parent = queue.popleft()
                parent.left = node 
            if node: queue.append(node)
        return root 