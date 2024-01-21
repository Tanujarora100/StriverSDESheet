class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def inorder_successor(root, target):
    successor = None

    while root:
        if root.val > target:
            successor = root
            root = root.left
        else:
            root = root.right

    return successor

# Example usage:
# Assuming root is the root node of the BST and target is the node for which we want to find the successor
# Create a BST for example
root = TreeNode(15)
root.left = TreeNode(10)
root.right = TreeNode(20)
root.left.left = TreeNode(8)
root.left.right = TreeNode(12)
root.right.left = TreeNode(16)
root.right.right = TreeNode(25)

target_node = root.left.left  # Assuming the target node is 8

result = inorder_successor(root, target_node.val)

if result:
    print("Inorder Successor of", target_node.val, "is", result.val)
else:
    print("No Inorder Successor found.")
