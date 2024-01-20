from collections import deque


class Solution:
    # Function to return the level order traversal of a tree.
    def levelOrder(self, root):
        if root is None:
            return None
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ans