# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        sum_val = 0
        if root.val > L:
            sum_val += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            sum_val += self.rangeSumBST(root.right, L, R)
        if L <= root.val <= R:
            sum_val += root.val
        return sum_val
