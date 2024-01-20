# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        queue = deque()
        if not root:
            return 0
        queue.append(root)
        count = 0
        while queue:
            queue_size = len(queue)
            count += queue_size
            for i in range(queue_size):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.popleft()
        return count

# Example Usage:
# Create a sample binary tree
#      1
#     / \
#    2   3
#   / \ / \
#  4  5 6  7
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))

# Create a Solution instance and count the nodes in the binary tree
solution = Solution()
result = solution.countNodes(root)

print("Total Nodes:", result)
