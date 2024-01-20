# Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    result = []

    def left(root, level):
        if root is None:
            return None
        if len(result) == level:
            result.append(root.data)
        left(root.left, level+1)
        left(root.right, level+1)
    left(root, 0)
    return result
    # code here