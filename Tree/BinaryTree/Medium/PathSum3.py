from collections import defaultdict

from Tree.BinaryTree.Easy.IterativePostOrder import TreeNode

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        hash_map = defaultdict(int)
        hash_map[0] = 1  # Initialize the prefix sum dictionary with 0 count
        count = 0

        def dfs(node, targetSum, curr_sum):
            nonlocal count
            if not node:
                return

            curr_sum += node.val
            count += hash_map.get(curr_sum - targetSum,0)
            hash_map[curr_sum] += 1

            dfs(node.left, targetSum, curr_sum)
            dfs(node.right, targetSum, curr_sum)

            hash_map[curr_sum] -= 1
            curr_sum-=node.val

        dfs(root, targetSum, 0)
        return count