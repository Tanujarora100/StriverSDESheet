# Definition for a binary tree node.
# from typing import Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional

from Tree.BinaryTree.Easy.IterativePostOrder import TreeNode


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return
        if root.val < low:
            return self.trimBST(root.right, low, high)
        # Ignore all the left values of the root node as if this node is smaller eveyrthing left will be smaller.
        elif root.val > high:
            # Ignore the right values every value can be ignored
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root