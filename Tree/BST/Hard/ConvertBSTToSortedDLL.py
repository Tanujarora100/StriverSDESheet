class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return None

        # Helper function to perform in-order traversal and convert to doubly linked list
        def in_order_traversal(node):
            nonlocal first, last

            if node:
                # Recursively process the left subtree
                in_order_traversal(node.left)

                # Update links for the current node
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node  # Set the head of the doubly linked list

                last = node  # Update the last visited node

                # Recursively process the right subtree
                in_order_traversal(node.right)

        # Initialize variables to keep track of the first and last nodes
        first, last = None, None

        # Perform in-order traversal to convert to doubly linked list
        in_order_traversal(root)

        # Connect the head and tail of the linked list
        first.left = last
        last.right = first

        return first  # Return the head of the doubly linked list


