# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import List, Optional

from Tree.BinaryTree.Easy.DiameterTree import TreeNode
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hash_map=defaultdict(int)
        max_freq=0
        def valid(root):
            nonlocal hash_map, max_freq
            if root is None:
                return 
            hash_map[root.val]+=1
            max_freq=max(max_freq,hash_map[root.val])
            valid(root.left)
            valid(root.right)
        valid(root)
        ans=[]
        for keys,values in hash_map.items():
            if values==max_freq:
                ans.append(keys)
        return ans