# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # If either root is empty, return the other root
        if not root1:
            return root2
        if not root2:
            return root1

        # Create a new node with the sum of values from root1 and root2
        merged_root = TreeNode(root1.val + root2.val)
        
        # Recursively merge the left subtrees of root1 and root2
        merged_root.left = self.mergeTrees(root1.left, root2.left)
        
        # Recursively merge the right subtrees of root1 and root2
        merged_root.right = self.mergeTrees(root1.right, root2.right)

        # Return the merged root
        return merged_root


