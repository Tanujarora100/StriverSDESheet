# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff= float('inf')
        prev_val=None
        def helper(root):
            nonlocal prev_val, min_diff
            if root is None:
                return None
            helper(root.left)
            if prev_val is not None:
                min_diff= min(min_diff, root.val-prev_val)
            prev_val=root.val
            helper(root.right)
            return root
        # node_list=sorted(node_list)
        helper(root)
        # print(node_list)
        return int(min_diff)