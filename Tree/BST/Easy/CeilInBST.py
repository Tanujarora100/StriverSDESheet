# User function to return the ceil of given number in BST.
def find_ceil(root, input):
    if root is None:
        return -1

    # Your code here
    ceil_val = -1
    while root:
        if root.data == input:
            ceil_val = root.data
            return ceil_val
        if input > root.data:
            root = root.right
        else:
            ceil_val = root.data
            root = root.left

    return ceil_val
