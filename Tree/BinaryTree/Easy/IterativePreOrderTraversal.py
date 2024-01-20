class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def iterative_preorder(root):
    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

    return result

# Example Usage:
# Create a sample binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

# Perform iterative preorder traversal
result = iterative_preorder(root)
print("Iterative Preorder Traversal:", result)
