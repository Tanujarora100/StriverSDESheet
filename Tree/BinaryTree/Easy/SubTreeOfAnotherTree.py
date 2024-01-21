class Solution:
    def isSubtree(self, root, subRoot):
        if root is None:
            return False
        if self.dfs(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def dfs(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        if root.val != subRoot.val:
            return False
        return self.dfs(root.left, subRoot.left) and self.dfs(root.right, subRoot.right)
