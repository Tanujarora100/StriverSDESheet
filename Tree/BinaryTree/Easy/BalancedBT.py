# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Tree.BinaryTree.Easy.DiameterTree import TreeNode


class Solution:
    
    balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None: return True
        self.height(root)
        return self.balanced
    
    def height(self, root):
        if (root == None): return 0
        l = self.height(root.left)
        r = self.height(root.right)
        if (abs(l-r) > 1):
            self.balanced = False
        return max(l, r)+1
        