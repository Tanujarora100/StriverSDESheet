def verify_preorder(preorder):
    stack = []
    lower_bound = float('-inf')

    for node in preorder:
        if node < lower_bound:
            return False

        while stack and node > stack[-1]:
            lower_bound = stack.pop()

        stack.append(node)

    return True

# Example usage:
# Assuming preorder is the list representing the preorder traversal of a BST
preorder_sequence = [5, 2, 1, 3, 6]

if verify_preorder(preorder_sequence):
    print("The given sequence is a valid preorder traversal of a BST.")
else:
    print("The given sequence is not a valid preorder traversal of a BST.")
