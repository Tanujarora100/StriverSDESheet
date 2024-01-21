from typing import Optional

from Tree.BinaryTree.Easy.IterativeInorder import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif root.val==key:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # Find the inorder successor (smallest value in the right subtree)
                successor = self.find_min_value(root.right)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
        return root

    def find_min_value(self, root):
        while root.left is not None:
            root = root.left
        return root