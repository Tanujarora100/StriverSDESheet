class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        # Define a helper function to traverse the tree and check for BST properties
        def helper(node):
            # Base case: if the current node is None, return 0 and the minimum and maximum possible values
            if not node:
                return 0, float('inf'), float('-inf')

            # Recursively call the helper function for the left and right subtrees
            left_size, left_min, left_max = helper(node.left)
            right_size, right_min, right_max = helper(node.right)

            # Check if the current node's value satisfies the BST property
            if left_max < node.val < right_min:
                size = left_size + right_size + 1
                return size, min(left_min, node.val), max(right_max, node.val)
            else:
                return max(left_size, right_size), float('-inf'), float('inf')

        # Call the helper function on the root node and return the size of the largest BST subtree
        size, _, _ = helper(root)
        return size

