# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maximum_ans = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.solve(root)
        return self.maximum_ans

    def solve(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.solve(root.left)
        right = self.solve(root.right)
        self.maximum_ans = max(self.maximum_ans, left + right)
        return 1 + max(left, right)

# Example Usage:
# Create a sample binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

# Perform diameter of binary tree
result = Solution().diameterOfBinaryTree(root)
print("Diameter of Binary Tree:", result)
