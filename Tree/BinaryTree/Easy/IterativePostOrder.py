class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def iterative_postorder(root):
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            if current.right:
                stack.append(current.right)
            stack.append(current)
            current = current.left

        current = stack.pop()

        if stack and current.right == stack[-1]:
            stack[-1] = current
            current = None
        else:
            result.append(current.val)
            current = None

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

# Perform iterative postorder traversal
result = iterative_postorder(root)
print("Iterative Postorder Traversal:", result)
