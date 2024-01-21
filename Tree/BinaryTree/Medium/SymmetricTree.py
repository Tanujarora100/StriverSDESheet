
from typing import Optional

from Tree.BinaryTree.Easy.IterativeInorder import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Create a mirrored version of the original tree
        mirror_node = self.create_mirror(root)
        
        # Compare the original tree with its mirrored version to check for symmetry
        return self.compare_mirror_tree(root, mirror_node)
        
    
    def create_mirror(self,root):
        if root is None:
            return None
        self.create_mirror(root.left)
        self.create_mirror(root.right)
        temp=root.left
        root.left=root.right
        root.right=temp
        return root
    
    
    def compare_mirror_tree(self,root1,root2):
        if root1 is None and root2 is None:
            return True
            # Both are Null so it is a mirror tree
        elif root1 is None or root2 is None:
            return False
        return root1.val==root2.val and self.compare_mirror_tree(root1.left,root2.right) and  self.compare_mirror_tree(root2.left,root1.right)
    