# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import List, Optional

from Tree.BinaryTree.Easy.IterativeInorder import TreeNode
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #    def buildTree(self, preorder, inorder):
        def Solve(inorder_start, inorder_end):
            nonlocal postorderIndex
            if inorder_start > inorder_end or postorderIndex < 0:
                return None
            rootData = postorder[postorderIndex]
            root = TreeNode(rootData)
            postorderIndex -= 1
            root.right = Solve(hash_map[rootData] + 1, inorder_end)
            root.left = Solve(inorder_start, hash_map[rootData] - 1)

            return root

        postorderIndex = len(postorder)-1
        hash_map = defaultdict(int)
        for index, values in enumerate(inorder):
            hash_map[values] = index
        return Solve(0, len(inorder) - 1)