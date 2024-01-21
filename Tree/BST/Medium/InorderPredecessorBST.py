class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def inorder_predecessor(root, target):
    predecessor = None

    while root:
        if root.val < target:
            predecessor = root
            root = root.right
        else:
            root = root.left

    return predecessor

# Example usage:
# Assuming root is the root node of the BST and target is the node for which we want to find the predecessor
# Create a BST for example
root = TreeNode(15)
root.left = TreeNode(10)
root.right = TreeNode(20)
root.left.left = TreeNode(8)
root.left.right = TreeNode(12)
root.right.left = TreeNode(16)
root.right.right = TreeNode(25)

target_node = root.left.right  # Assuming the target node is 12

result = inorder_predecessor(root, target_node.val)

if result:
    print("Inorder Predecessor of", target_node.val, "is", result.val)
else:
    print("No Inorder Predecessor found.")
