from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        max_sum = -float('inf')
        max_level_sum = -1
        count = 1
        while queue:
            curr_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                curr_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_level_sum = count
            count = count+1
        return max_level_sum