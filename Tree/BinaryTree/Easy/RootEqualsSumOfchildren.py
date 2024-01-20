# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Tree.BinaryTree.LCA2 import TreeNode


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
      return root.val == (root.left.val + root.right.val)