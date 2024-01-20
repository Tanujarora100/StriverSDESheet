# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from Tree.BinaryTree.PreOrderTraversal import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      res= []
      def postOrder(self,root):
        if root is None:
          return
        postOrder(self,root.left)
        postOrder(self,root.right)
        res.append(root.val)
      postOrder(self,root)
      return res
        