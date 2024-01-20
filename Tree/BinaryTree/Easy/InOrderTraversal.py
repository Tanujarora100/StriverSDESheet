# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from Tree.BinaryTree.PreOrderTraversal import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]

        def solve(root):
            if root is None:
                return
            solve(root.left)
            ans.append(root.val)
            solve(root.right)
        solve(root)
        return ans