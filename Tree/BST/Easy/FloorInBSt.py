# User function to return the floor of given number in BST.
def find_floor(root, input):
    if root is None:
        return -1

    # Your code here
    floor_val = -1
    while root:
        if root.data == input:
            floor_val = root.data
            return floor_val
        if input < root.data:
            root = root.left
        else:
            floor_val = root.data
            root = root.right

    return floor_val
