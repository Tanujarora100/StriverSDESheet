# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from Tree.BinaryTree.Easy.IterativePostOrder import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower_bound= -float('inf')
        upper_bound=float('inf')
        def solve(root,lower_bound,upper_bound):
            if root is None:
                return True
            if lower_bound<root.val<upper_bound:
                return solve(root.left,lower_bound,root.val) and solve(root.right,root.val,upper_bound)
            else:
                return False
            
        return solve(root,lower_bound,upper_bound)