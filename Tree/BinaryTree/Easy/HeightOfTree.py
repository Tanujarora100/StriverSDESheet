class Solution:
    # Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if root is None:
            return 0
        rh = self.height(root.left)
        lh = self.height(root.right)
        return 1 + max(rh, lh)