# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
import collections
from typing import List

from Tree.BinaryTree.IterativeInorder import TreeNode

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = collections.deque([root])
        res = []
        even_level = False
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                if even_level:
                    # pop from right and append from left.
                    node = queue.pop()
                    # to maintain the order of nodes in the format of [left, right, left, right] 
                    # we push right first since we are appending from left
                    if node.right: queue.appendleft(node.right)
                    if node.left: queue.appendleft(node.left)
                else:
                    # pop from left and append from right
                    node = queue.popleft()
                    # here the order is maintained in the format [left, right, left, right] 
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                level.append(node.val)
            res.append(level)
            even_level = not even_level
        return res