from typing import Optional


class TreeNode:
    def __init__(self, val=None, right=None, left=None) -> None:
        self.val = val
        self.right = right
        self.left = left


def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return root
    root.left = self.pruneTree(root.left)
    root.right = self.pruneTree(root.right)
    if root.val == 0 and root.left == None and root.right == None:
        root = None
    return root