# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from Tree.BinaryTree.Easy.IterativeInorder import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        ans=[]
        def dfs(root,temp):
            nonlocal ans
            if root is None:
                return
            temp+=str(root.val)+( "->")
            if not root.left and not root.right:
                temp=temp[:-2]
                ans.append(temp)
                return
            dfs(root.left,temp)
            dfs(root.right,temp)
            temp=temp[:-1]
            return root
        dfs(root,"")
        return ans