from typing import Optional
from Tree.BinaryTree.Easy.IterativePostOrder import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        inorder_ans = []
        
        def inorder(root):
            nonlocal inorder_ans
            if root is None:
                return
            inorder(root.left)
            inorder_ans.append(root.val)
            inorder(root.right)
            return root
        
        inorder(root)
        inorder_ans.sort()
        def swap_nodes(root):
            nonlocal inorder_ans, inorder_index
            if root is None:
                return
            swap_nodes(root.left)
            if root.val!=inorder_ans[inorder_index]:
                root.val=inorder_ans[inorder_index]
            inorder_index+=1
            swap_nodes(root.right)
            return root
        inorder_index=0
        swap_nodes(root)


