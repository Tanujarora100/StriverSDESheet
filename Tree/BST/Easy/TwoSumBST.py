from typing import Optional

from Tree.BinaryTree.Easy.IterativeInorder import TreeNode


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.helper(root, k, set())
        
    def helper(self, root, k, seen):
        if not root:
            return None
        if (k - root.val) in seen:
            return True
        seen.add(root.val)
        left = self.helper(root.left, k, seen)
        right = self.helper(root.right, k, seen)
        
        return left or right