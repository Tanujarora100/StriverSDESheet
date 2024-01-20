# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maximum_sum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.maximum_sum

    def helper(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))

        self.maximum_sum = max(self.maximum_sum, left + right + root.val)
        return root.val + max(left, right)

# Example Usage:
# Create a sample binary tree
#      -10
#      / \
#     9  20
#        / \
#       15  7
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

# Create a Solution instance and find the maximum path sum
solution = Solution()
result = solution.maxPathSum(root)
print("Maximum Path Sum:", result)
