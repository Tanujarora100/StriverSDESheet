# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from Tree.BinaryTree.Hard.CountCompleteTreeNodes import TreeNode


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        lower=-float('inf')
        higher= float('inf')
        preIndex=0
        def dfs(lower,higher):
            nonlocal preIndex
            if preIndex>=len(preorder):
                return None
            root_value= preorder[preIndex]
            if lower<root_value<higher:
                preIndex+=1
                root=TreeNode(root_value)
                root.left= dfs(lower,root_value)
                root.right=dfs(root_value,higher)
                return root
            else:
                return None
        return dfs(lower,higher)