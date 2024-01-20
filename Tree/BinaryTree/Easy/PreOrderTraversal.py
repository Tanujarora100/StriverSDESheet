# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer=[]
        def pre_order(root):
            if not root:
                return None
            answer.append(root.val)
            pre_order(root.left)
            pre_order(root.right)
        pre_order(root)
        return answer
      