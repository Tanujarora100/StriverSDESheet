class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root is None:
        return None

    if root is p or root is q:
        return root

    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    elif left:
        return left
    elif right:
        return right
    else:
        return None


def lowest_common_iterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    stack = [(root, [root])]

    # Variables to track node paths
    path_p = None
    path_q = None

    # Perform iterative depth-first search until both p and q are found
    while stack and (path_p is None or path_q is None):
        node, path = stack.pop()

        if node == p:
            path_p = path
        if node == q:
            path_q = path

        # Explore the left and right subtrees
        if node.right:
            stack.append((node.right, path + [node.right]))
        if node.left:
            stack.append((node.left, path + [node.left]))

    # Find the LCA from the obtained paths
    if path_p is None or path_q is None:
        return None

    lca = None
    i = 0
    while i < min(len(path_p), len(path_q)) and path_p[i] == path_q[i]:
        lca = path_p[i]
        i += 1

    return lca