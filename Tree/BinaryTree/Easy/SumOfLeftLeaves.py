# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Tree.BinaryTree.Easy.DiameterTree import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
      self.total=0
      
      def dfs(node,left):
        if node is None:
          return
        dfs(node.left,True)
        dfs(node.right,False)

        if(not node.left and not node.right and left):
          self.total+=node.val
            
      dfs(root,False)
      return self.total
            