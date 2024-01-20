class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.count = 0
        result = self.found(root, p, q)
        return result if self.count == 2 else None

    def found(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None

        left = self.found(root.left, p, q)
        right = self.found(root.right, p, q)

        if root.val == p.val or root.val == q.val:
            self.count += 1
            return root

        if left and right:
            return root

        return left if left else right