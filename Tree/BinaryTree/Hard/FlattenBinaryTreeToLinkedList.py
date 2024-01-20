# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Handle the null scenario
        if not root:
            return

        node = root

        while node:
            # If the node has a left child
            if node.left:
                # Find the rightmost node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right

                # Rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None

            # Move on to the right side of the tree
            node = node.right

# Example Usage:
# Create a sample binary tree
#      1
#     / \
#    2   5
#   / \   \
#  3   4   6
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))

# Create a Solution instance and flatten the binary tree
solution = Solution()
solution.flatten(root)

# Print the flattened tree
while root:
    print(root.val, end=" ")
    root = root.right
