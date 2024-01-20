from collections import defaultdict
from Tree.BinaryTree.Easy.IterativeInorder import TreeNode


class Solution:
    def buildTree(self, preorder, inorder):
        def Solve(inorder_start, inorder_end):
            nonlocal preOrderIndex
            if inorder_start > inorder_end or preOrderIndex >= len(inorder):
                return None
            rootData = preorder[preOrderIndex]
            root = TreeNode(rootData)
            preOrderIndex += 1

            root.left = Solve(inorder_start, hash_map[rootData] - 1)
            root.right = Solve(hash_map[rootData] + 1, inorder_end)

            return root

        preOrderIndex = 0
        hash_map = defaultdict(int)
        for index, values in enumerate(inorder):
            hash_map[values] = index
        return Solve(0, len(inorder) - 1 )